"""

    """

from mirutil.latex import ret_pathes_4_latex_dirtree_forest


class Param :
    root_dir = '/Users/mahdi/Library/CloudStorage/OneDrive-khatam.ac.ir/Heidari Data/V2'
    gitignore_file = '/Users/mahdi/Library/CloudStorage/OneDrive-khatam.ac.ir/Heidari Data/V2/.gitignore'

p = Param()

def main() :
    pass

    ##
    fu = ret_pathes_4_latex_dirtree_forest
    res = fu(p.root_dir , p.gitignore_file , only_dirs = True)
    print(res)

    ##
    with open('res.txt' , 'w') as fi :
        fi.write(res)
        print('saved as res.txt')

    ##

##
if __name__ == "__main__" :
    main()
    print('Done!')
