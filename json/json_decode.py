import getopt, sys
import urllib.parse


if __name__ == "__main__":
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, 'd:')
    except getopt.GetoptError:
        print('Error: {}'.format(getopt.GetoptError))
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-d':
            data = arg
            temp = urllib.parse.unquote(data)
            decode_data = urllib.parse.unquote_plus(temp)
            print (decode_data)
        else:
            print ('python3 json_decode.py -d <data>')
            sys.exit(2)