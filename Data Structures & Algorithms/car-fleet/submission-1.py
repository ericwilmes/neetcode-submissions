class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_to_arrive = {}
        output = 0
        data = []

        for i in range(len(position)):
            pos = position[i]
            sp = speed[i]
            time_to_end = (target - pos) / sp
            data.append((pos, sp, time_to_end))

            pos_to_arrive[pos] = time_to_end
        data_sorted = sorted(data, key=lambda x: x[0], reverse=True)
        print(data_sorted)

        fleet_time = 0

        for d in data_sorted:
            time = d[2]
            print(time, fleet_time)
            if fleet_time == 0:
                fleet_time = time
                output += 1
            if time <= fleet_time:
                fleet_time = max(time, fleet_time)
            else:
                output += 1
                fleet_time = time

        return output