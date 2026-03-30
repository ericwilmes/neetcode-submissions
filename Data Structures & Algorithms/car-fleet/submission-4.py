class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        output = 0
        data = []

        for i in range(len(position)):
            pos = position[i]
            sp = speed[i]
            time_to_end = (target - pos) / sp
            data.append((pos, sp, time_to_end))
        data_sorted = sorted(data, key=lambda x: x[0], reverse=True)

        fleet_time = None
        for _, _, time in data_sorted:
            if fleet_time and time <= fleet_time:
                continue
            output += 1
            fleet_time = time

        return output