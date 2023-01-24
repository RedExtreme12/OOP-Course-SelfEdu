class Model:

    def __init__(self):
        self.fields = {}

    def query(self, **k_fields):
        self.fields.update(k_fields)

    def __str__(self):
        if self.fields:
            fields = ', '.join(f'{k} = {v}' for k, v in self.fields.items())
            return f'Model: {fields}'
        return 'Model'


model = Model()
# model.query(id=1, fio='Sergey', old=33)
print(str(model))
