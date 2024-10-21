class effect:
    def __init__(
        self,
    ):
        pass


class monster:
    def __init__(
        self,
        id: str,
        data: dict[
            str,
            list[
                dict[
                    str,
                    list[str]
                    | int
                    | bool
                    | None
                    | str
                    | tuple[str | bool | int, str | bool | int],
                ]
            ],
        ],
    ):
        self.id = id


class mash:
    def __init__(
        self,
    ):
        pass


class manager:
    def __init__(
        self,
    ):
        pass
