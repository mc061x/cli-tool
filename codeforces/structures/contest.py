from system.structures.dummyStruct import DummyStruct


class Contest(DummyStruct):
    def __init__(self) -> None:
        super().__init__()
        self.id = int()
        self.name = str()
        self.type = str()
        self.phase = str()
        self.frozen = bool()
        self.durationSeconds = int()
        self.startTimeSeconds = int()
        self.relativeTimeSeconds = int()
        self.preparedBy = str()
        self.websiteUrl = str()
        self.difficulty = int()
        self.kind = str()
        self.icpcRegion = str()
        self.country = str()
        self.city = str()
        self.season = str()
