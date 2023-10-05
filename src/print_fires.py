import my_utils as mu
import argparse as ap
import sys


def get_args():
    parser = ap.ArgumentParser(description='Command Line parser written in python',
                                prog = 'print_fires')
    
    parser.add_argument('--f',
                       type = str,
                       help='Name of file',
                       required=True)
    
    parser.add_argument('--cc',
                       type = int,
                       help='Country Column',
                       required=True)
    
    parser.add_argument('--c',
                       type = str,
                       help='Country',
                       required=True)
    
    parser.add_argument('--fc',
                       type = int,
                       help='Fires Column',
                       required=True)
    
    return parser.parse_args()




def main():
    args = get_args()

    file_name = args.f
    country_column = args.cc
    country= args.c
    fires_column = args.fc

    fires = mu.get_column(file_name, country_column, country, result_column=fires_column)
    print(fires)
    
    if fires == []:
        sys.exit(1)

if __name__ == '__main__':
    main()

