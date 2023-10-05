test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run print_fires_no_op_us python src/print_fires.py --f 'test/data/Agrofood_co2_emission_ft.csv' --cc 1 --c 'United States of America' --fc 4
assert_in_stdout [1999, 1999, 1999, 1999, 1999, 1999, 3286, 1553, 3099, 3578, 3687, 534, 1475, 1224, 1201, 915, 1086, 1558, 2068, 1093, 912, 1330, 1173, 1284, 1336, 2235, 1438, 2664, 2457, 1190, 5405]
assert_exit_code 0

run print_fires_mean_us python src/print_fires.py --f 'test/data/Agrofood_co2_emission_ft.csv' --cc 1 --c 'United States of America' --fc 4 --op mean
assert_in_stdout 1928.225806451613
assert_exit_code 0

run print_fires_median_us python src/print_fires.py --f 'test/data/Agrofood_co2_emission_ft.csv' --cc 1 --c 'United States of America' --fc 4 --op median
assert_in_stdout 1558.0
assert_exit_code 0

run print_fires_std_us python src/print_fires.py --f 'test/data/Agrofood_co2_emission_ft.csv' --cc 1 --c 'United States of America' --fc 4 --op std
assert_in_stdout 1007.7033520762149
assert_exit_code 0

run print_fires_no_op_japan python src/print_fires.py --f 'test/data/Agrofood_co2_emission_ft.csv' --cc 1 --c 'Japan' --fc 4
assert_in_stdout [13, 13, 13, 13, 13, 13, 16, 12, 12, 14, 16, 8, 12, 10, 5, 11, 9, 18, 24, 7, 8, 14, 5, 7, 38, 11, 4, 12, 21, 19, 19]
assert_exit_code 0

run print_fires_mean_japan python src/print_fires.py --f 'test/data/Agrofood_co2_emission_ft.csv' --cc 1 --c 'Japan' --fc 4 --op mean
assert_in_stdout 13.225806451612904
assert_exit_code 0

run print_fires_median_japan python src/print_fires.py --f 'test/data/Agrofood_co2_emission_ft.csv' --cc 1 --c 'Japan' --fc 4 --op median
assert_in_stdout 13.0
assert_exit_code 0

run print_fires_std_japan python src/print_fires.py --f 'test/data/Agrofood_co2_emission_ft.csv' --cc 1 --c 'Japan' --fc 4 --op std
assert_in_stdout 6.459350199114233
assert_exit_code 0

run print_fires_std_japan_index_out_of_bounds python src/print_fires.py --f 'test/data/Agrofood_co2_emission_ft.csv' --cc 1 --c 'Japan' --fc 400 --op std
assert_exit_code 1

run print_fires_no_op_australia_file_not_found python src/print_fires.py --f 'test/data/Agrofood_co2_emission_fts.csv' --cc 1 --c 'Australia' --fc 4
assert_exit_code 1
