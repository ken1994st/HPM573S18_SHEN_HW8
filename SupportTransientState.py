import scr.FormatFunctions as Format
import scr.StatisticalClasses as Stat
import Parameters as P


def print_outcomes(multi_cohort, name):
    """ prints the outcomes of a simulated cohort under steady state
    :param multi_cohort: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and confidence interval text of patient survival time
    reward_mean_PI_text = Format.format_estimate_interval(
        estimate=multi_cohort.get_mean_total_reward(),
        interval=multi_cohort.get_PI_total_reward(alpha=P.ALPHA),
        deci=1)

    # print survival time statistics
    print(name)
    print("Estimate of mean rewards and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          reward_mean_PI_text)



def print_comparative_outcomes(multi_cohort_ONE, multi_cohort_TWO):
    """ prints expected and percentage increase in average survival time when drug is available
    :param multi_cohort_no_drug: multiple cohorts simulated when drug is not available
    :param multi_cohort_with_drug: multiple cohorts simulated when drug is available
    """

    # increase in survival time
    increase = Stat.DifferenceStatIndp(
        name='Increase in total rewards',
        x=multi_cohort_ONE.get_all_total_rewards(),
        y_ref=multi_cohort_TWO.get_all_total_rewards()
    )
    # estimate and prediction interval
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_PI(alpha=P.ALPHA),
        deci=1
    )
    print("Expected increase in total rewards and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

