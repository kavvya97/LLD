from lru_policy import LruPolicy
from hashmap_store import HashMapStore
from cache import Cache
def main():
    cache = Cache(LruPolicy(), HashMapStore(2))
    cache.put(1, "dsfasdf")
    cache.put(2, "poland")
    cache.get(1)
    cache.put(3, "kavs")
    value = cache.get(1)
    print(value)

if __name__ == "__main__":
    main()


https://medium.com/@narengowda/stock-exchange-system-design-answered-ad4be1345851
https://leetcode.com/discuss/interview-question/system-design/724254/System-design-Need-help-for-amazon-question
https://leetcode.com/discuss/interview-question/system-design/233869/Design-Amazon-Locker-system
https://leetcode.com/discuss/interview-question/system-design/138097/Design-Notification-Service-for-Amazon-Alexa
https://leetcode.com/discuss/interview-question/system-design/144287/Design-Recommendation-System-for-Amazon-Videos
https://leetcode.com/discuss/interview-question/system-design/769578/Amazon-orSystem-Design-or-Amazon-Go-or-suggestion-on-solution-welcome!!!