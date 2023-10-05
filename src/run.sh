#python print_fires.py  --This works
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 1 --c 'United States of America' --fc 4
echo $?


#python print_fires.py  --This should produce a File Not Found Error
python print_fires.py --f 'Agrofood_co2_emissions.csv' --cc 1 --c 'United States of America' --fc 4
echo $?


#python print_fires.py  --This should produce an Index out of range error
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 1 --c 'United States of America' --fc 400
echo $?

#python print_fires.py  --This should produce an Index out of range error
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 400 --c 'United States of America' --fc 4
echo $?



#python print_fires.py  --This should produce a could not convert value to an int error
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 1 --c 'United States of America' --fc 1
echo $?

#python print_fires.py  --This should produce a could not convert value to an int error
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 1 --c 'United States of America' --fc 4 --op mean
echo $?

#python print_fires.py  --This should produce a could not convert value to an int error
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 1 --c 'United States of America' --fc 4 --op median
echo $?

#python print_fires.py  --This should produce a could not convert value to an int error
python print_fires.py --f 'Agrofood_co2_emission.csv' --cc 1 --c 'United States of America' --fc 4 --op std
echo $?