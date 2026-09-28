class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        bilan = 0
        bilan_min = 0
        depart = 0

        for i in range(len(gas)):
            bilan += gas[i] - cost[i]

            if bilan < bilan_min:
                bilan_min = bilan
                depart = i + 1

        return depart