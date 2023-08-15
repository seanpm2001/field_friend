import rosys

from .plant import Plant


class PlantProvider:

    def __init__(self) -> None:
        self.weeds: list[Plant] = []
        self.crops: list[Plant] = []

        self.PLANTS_CHANGED = rosys.event.Event()
        """The collection of plants has changed."""

        self.ADDED_NEW_WEED = rosys.event.Event()
        """A new weed has been added."""

        self.ADDED_NEW_BEET = rosys.event.Event()
        """A new beet has been added."""

        rosys.on_repeat(self.prune, 10.0)

    def prune(self, max_age: float = 100 * 60.0) -> None:
        self.weeds[:] = [weed for weed in self.weeds if weed.detection_time > rosys.time() - max_age]
        self.crops[:] = [crop for crop in self.crops if crop.detection_time > rosys.time() - max_age]
        self.PLANTS_CHANGED.emit()

    def add_weed(self, weed: Plant) -> None:
        for w in self.weeds:
            if w.position.distance(weed.position) < 0.02 and w.type == weed.type:
                return
        self.weeds.append(weed)
        self.PLANTS_CHANGED.emit()
        self.ADDED_NEW_WEED.emit()

    def remove_weed(self, weed_id: str) -> None:
        self.weeds[:] = [weed for weed in self.weeds if weed.id != weed_id]
        self.PLANTS_CHANGED.emit()

    def clear_weeds(self) -> None:
        self.weeds.clear()
        self.PLANTS_CHANGED.emit()

    def add_crop(self, crop: Plant) -> None:
        for c in self.crops:
            if c.position.distance(crop.position) < 0.03 and c.type == crop.type:
                return
        self.crops.append(crop)
        self.PLANTS_CHANGED.emit()
        self.ADDED_NEW_BEET.emit()

    def remove_crop(self, crop: Plant) -> None:
        self.crops[:] = [c for c in self.crops if c.id != crop.id]
        self.PLANTS_CHANGED.emit()

    def clear_crops(self) -> None:
        self.crops.clear()
        self.PLANTS_CHANGED.emit()

    def clear(self) -> None:
        self.clear_weeds()
        self.clear_crops()
