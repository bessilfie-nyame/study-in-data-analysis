import familiar
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency
import numpy as np

vein_pack_lifespans = familiar.lifespans(package='vein')

vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
_, pvalue = vein_pack_test
print(pvalue)
if pvalue <= 0.05:
  print("The Vein Pack Is Proven To Make You Live Longer!")
else:
  print("The Vein Pack Is Probably Good For You Somehow!")

artery_pack_lifespans = familiar.lifespans(package='artery')
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
_, pval = package_comparison_results
print(pval)
if pval <= 0.05:
  print("Tthe Artery Package guarantees even stronger results!")
else:
  print("the Artery Package is also a great product!")
iron_contingency_table = familiar.iron_counts_for_package()
_, iron_pvalue, _, _ = chi2_contingency(iron_contingency_table)
print(iron_pvalue)
if iron_pvalue <= 0.05:
  print("The Artery Package Is Proven To Make You Healthier!")


