class DnDHitCalculator:
    def __init__(self, attack_modifier):
        self.attack_modifier = attack_modifier

    def calculate_hit_probability(self, enemy_ac):
        """
        Calculate the probability of hitting an enemy in D&D 5e.
        
        Parameters:
            enemy_ac (int): The enemy's Armor Class
            
        Returns:
            float: Probability of hitting (0.0 to 1.0)
        """
        # Need to roll this number or higher on d20
        required_roll = enemy_ac - self.attack_modifier
        
        # Count successful rolls (remember natural 20 always hits)
        successful_rolls = max(1, 21 - required_roll)  # At least 1 for nat 20
        
        # Probability is successful rolls / 20
        return successful_rolls / 20
    
    def calculate_effective_advantage_bonus(self, enemy_ac):
        """
        Calculate the effective attack bonus that advantage provides.
        
        Parameters:
            enemy_ac (int): The enemy's Armor Class
            
        Returns:
            float: Effective bonus to attack rolls that advantage provides
        """
        # Get probability of hitting with and without advantage
        prob_without_adv = self.calculate_hit_probability(enemy_ac)
        prob_with_adv = 1 - ((1 - prob_without_adv) ** 2)
        
        # Find what attack bonus would give us the same probability
        # Start with current attack modifier and increase until we match or exceed
        test_calculator = DnDHitCalculator(self.attack_modifier)
        bonus = 0
        
        while test_calculator.calculate_hit_probability(enemy_ac) < prob_with_adv:
            bonus += 1
            test_calculator = DnDHitCalculator(self.attack_modifier + bonus)
            
        return float(bonus)
    
# Test the code
if __name__ == "__main__":
    calculator = DnDHitCalculator(attack_modifier=5)
    enemy_ac = 15
    
    probability = calculator.calculate_hit_probability(enemy_ac)
    print(f"Probability of hitting AC {enemy_ac}: {probability:.1%}")
    
    effective_bonus = calculator.calculate_effective_advantage_bonus(enemy_ac)
    print(f"Advantage is equivalent to about a +{effective_bonus:.1f} bonus to hit")