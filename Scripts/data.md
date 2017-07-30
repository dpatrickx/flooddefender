### Flow Entry Utilization

|       Models      | Normal User |   Attacker  | All Entries  |
| Native Floodlight |  616.75-31% | 1072.18-54% | 1697.89-85%  |
|    FloodDefender  |  376.42-19% |  152.45-8%  |  962.60-48%  |
|    FloodShield    |  626.64-31% |   87.67-4%  |  717.10-36%  |

FloodDefender:
    + more space: monitoring rules in flow table region
    + less normal rules: There will be a monitoring rule installed into flow table region every time a processing rule is installed in cache region, makes normal rules in flow table region easier to be evicted.

### Normal User Flow-Removed

|      Models       | Average Eviction Time |
| Native Floodlight |         115.98        |
|    FloodDefender  |         146.06        |
|    FloodShield    |         119.49        |
