#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,argparse,random,string
from time import gmtime, strftime
parser =argparse.ArgumentParser(
    description="Provide three random 12 characters strings by default",
    formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=150,width=150))
parser.add_argument('-l','--lenth',help='The longth about you wanted (default 12)',default=12,type=int)
parser.add_argument('-n','--amount',help='The amount about you wanted (default 1)',default=1,type=int)
parser.add_argument('-s','--save',help='If save to a file (~/.randomstring.txt)',type=str)
group=parser.add_mutually_exclusive_group()
group.add_argument('-A','--all',help='Incloud digits letters and punnctuaion',action='store_true')
group.add_argument('-N','--number',help='Number and letters',action='store_true')


args= parser.parse_args()

def randomcharacter(lenth):
    letters ="".join(random.sample(list(string.ascii_letters[:]),lenth))
    hexdigits ="".join(random.sample(list(string.hexdigits), lenth))
    punctuation = random.sample(string.punctuation, 9)
    Punctuation ="".join(random.sample(punctuation + list(string.ascii_letters[:]), lenth))

    if args.all :
        return Punctuation
    if args.number:
        return hexdigits
    else:
        return letters

def main():
    try:
        home = os.path.expanduser("~")
        with open ('{}/{}randomstring.txt'.format(home,'.'),'a',encoding='utf-8-sig') as f:
            pass
    except Exception as e :
        print('无法创建{}'.format(e))
        exit()

    lenth=args.lenth
    remark=args.save
    for i in range(args.amount):
        text=randomcharacter(lenth)
        info='{}\t {}\t{}\n'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),text,remark)
        if args.save:
            with open ('{}/{}randomstring.txt'.format(home,'.'),'a',encoding='utf-8-sig') as f:
                f.writelines(info)
                print (text)
        else :
            print (text)   

if __name__ =='__main__':
    main()