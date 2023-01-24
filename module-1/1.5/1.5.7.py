class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr  # frequency


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu: CPU, mem_slots, total_mem_slots=4):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots[:total_mem_slots]
        self.total_mem_slots = total_mem_slots

    def _get_memory_info(self):
        return ' '.join([f'{memory_obj.name} - {memory_obj.volume};' for memory_obj in self.mem_slots]).rstrip(';')

    def get_config(self):
        info = [
            f'Материнская плата: {self.name}',
            f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
            f'Слотов памяти: {self.total_mem_slots}',
            f'Память: {self._get_memory_info()}'
        ]

        return info


mem1 = Memory(
    'Kingston1',
    2
)

mem2 = Memory(
    'Kingston2',
    2
)

mb = MotherBoard(
    'MSI',
    CPU(
        'AMD',
        3.8
    ),
    [
        mem1,
        mem2,
    ]
)
