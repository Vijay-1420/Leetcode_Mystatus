class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        

        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        pq = [(0, k)]

        while pq:
            time, node = heapq.heappop(pq)

            if time > dist[node]:
                continue

            for nei, weight in graph[node]:
                new_time = time + weight

                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(pq, (new_time, nei))

        ans = max(dist[1:])

        if ans == float('inf'):
            return -1

        return ans
