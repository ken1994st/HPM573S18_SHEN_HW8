import Parameters as P
import HW8 as Cls
import SupportSteadyState as Support


cohortONE = Cls.SetOfGames(
    id=1,
    n_games=P.SIM_POP_SIZE,
    prob_head=0.5)
# simulate the cohort
OutcomeONE = cohortONE.simulation()


cohortTWO = Cls.SetOfGames(
    id=2,
    n_games=P.SIM_POP_SIZE,
    prob_head=0.45)
# simulate the cohort
OutcomeTWO = cohortTWO.simulation()

# print outcomes of each cohort
Support.print_outcomes(OutcomeONE, 'When coin with 0.5:')
Support.print_outcomes(OutcomeTWO, 'When coin with 0.45:')


# print comparative outcomes
Support.print_comparative_outcomes(OutcomeONE, OutcomeTWO)
