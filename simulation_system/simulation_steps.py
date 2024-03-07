# simulation_system/simulation_steps
from enum import Enum

class Simulation_Step(Enum):
    OnStartStatusUpdate = 1
    OnInitiation = 2
    BeforeDealDamage = 3
    OnDealDamage = 4
    BeforeDealBonusDamage = 5
    OnDealBonusDamage = 6
    BeforeAutoAttack = 7
    OnAutoAttack = 8
    BeforeCastUltimate = 9
    OnCastUltimate = 10
    OnEndStatusUpdate = 11
    OnDealHealing = 12
    BeforeDealHealing = 13
    OnHeal = 14
    BeforeHeal = 15
    OnDealShielding = 16
    BeforeDealShielding = 17
    OnGainShield = 18
    BeforeGainShield = 19