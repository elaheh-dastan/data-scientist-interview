"""
Trip Forecast at Picnic
Picnic wishes to forecast how many trips are required to deliver all customer
orders and optimize people planning. Planning too many people is a waste of
money, and planning not enough people will limit the number of deliveries we
can handle. To provide the most accurate forecast, we need to get constant
updates on how many orders do we forecast our customers will place. To
calculate it we have two sources, our delivery forecast and hub capacity. We
need to select the most constraining source to ensure accurate predictions.

## GET /v1/updates

Return delivery updates for all the hubs in the Netherlands. Poll-based: any
update will only be visible once.

Example response:
    [
      {'hub_id': 'DEV', 'deliveries': 5, 'source': 'forecast'},
      {'hub_id': 'DEV', 'deliveries': 20, 'source': 'forecast'},
      {'hub_id': 'EMM', 'deliveries': 5, 'source': 'forecast'},
      {'hub_id': 'DEV', 'deliveries': 17, 'source': 'capacity'},
      ...
    ]

| hub_id | deliveries |
|--------|------------|
|     DEV|          17|
|     EMM|          5 |

# The output table
The output table will be used by our forecasting model as features.
| hub_id | deliveries |
|--------|------------|
|     DEV|          17|
|     EMM|          24|
|     AMS|          18|
|     ...|         ...|
"""

from typing import Iterable, TypedDict


class Update(TypedDict):
    hub_id: str
    deliveries: int
    source: str


class Hub:
    def __init__(self, hub_id: str, forecast: int = 0, capacity: int = 0) -> None:
        self.hub_id = hub_id
        self.forecast = forecast
        self.capacity = capacity

    @property
    def deliveries(self) -> int:
        # the most constraining source is whichever one is lower; if we've
        # only ever seen one source for this hub, fall back to that one
        if self.forecast and self.capacity:
            return min(self.forecast, self.capacity)
        return self.forecast or self.capacity


class FeatureStore:
    """Accumulates poll-based delivery updates per hub and exposes the most
    constraining (forecast vs. capacity) delivery count as a feature."""

    def __init__(self) -> None:
        self._hubs: dict[str, Hub] = {}

    def apply_updates(self, updates: Iterable[Update]) -> None:
        for update in updates:
            hub = self._hubs.setdefault(update["hub_id"], Hub(update["hub_id"]))
            if update["source"] == "forecast":
                hub.forecast += update["deliveries"]
            else:
                hub.capacity += update["deliveries"]

    def as_table(self) -> list[dict[str, int | str]]:
        return [
            {"hub_id": hub.hub_id, "deliveries": hub.deliveries}
            for hub in self._hubs.values()
        ]


if __name__ == "__main__":
    updates: list[Update] = [
        {"hub_id": "DEV", "deliveries": 5, "source": "forecast"},
        {"hub_id": "DEV", "deliveries": 20, "source": "forecast"},
        {"hub_id": "EMM", "deliveries": 5, "source": "forecast"},
        {"hub_id": "DEV", "deliveries": 17, "source": "capacity"},
    ]

    store = FeatureStore()
    store.apply_updates(updates)
    for row in store.as_table():
        print(row)
