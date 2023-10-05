#This works - US
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 1 --c 'United States of America' --fc 4
echo $?

#This works - US
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 1 --c 'United States of America'
echo $?

#This should produce a File Not Found Error
python print_fires.py --f 'Agrofood_co2_emissions.csv' --cc 1 --c 'United States of America' --fc 4
echo $?


#This should produce an Index out of range error
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 1 --c 'United States of America' --fc 400
echo $?

#This should produce an Index out of range error
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 400 --c 'United States of America' --fc 4
echo $?

#This should produce a could not convert value to an int error
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 1 --c 'United States of America' --fc 1
echo $?

#This should give you the mean for US forest fires
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 1 --c 'United States of America' --fc 4 --op mean
echo $?

#This should give you the median for US forest fires
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 1 --c 'United States of America' --fc 4 --op median
echo $?

#This should give you the standard deviation for US forest fires
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 1 --c 'United States of America' --fc 4 --op std
echo $?

#This works - Japan
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 1 --c 'Japan' --fc 4
echo $?

#This should give you the mean for Japan forest fires
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 1 --c 'Japan' --fc 4 --op mean
echo $?

#This should give you the median for Japan forest fires
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 1 --c 'Japan' --fc 4 --op median
echo $?

#This should give you the standard deviation for Japan forest fires
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 1 --c 'Japan' --fc 4 --op std
echo $?