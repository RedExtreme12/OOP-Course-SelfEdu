class StreamData:

    def create(self, fields, lst_values) -> bool:
        if len(fields) != len(lst_values):
            return False

        for field, lst_value in zip(fields, lst_values):
            setattr(self, field, lst_value)

        return True
