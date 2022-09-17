"""

    """

import json
from pathlib import Path
import shutil

from githubdata import GithubData
from mirutil.latex import make_txt4_forest_tree


class GDUrl :
    with open('gdu.json' , 'r') as f :
        gj = json.load(f)

    src = gj['src']

gu = GDUrl()

class Param :
    root = '/Users/mahdi/Library/CloudStorage/OneDrive-khatam.ac.ir/Datasets/Heidari Data/V2'
    root_dir = Path(root)
    gitignore_file = root_dir / '.gitignore'

p = Param()

def main() :
    pass

    ##
    gs = GithubData(gu.src)
    gs.overwriting_clone()
    ##
    fp = gs.local_path / '.gitignore'
    nfp = p.gitignore_file
    shutil.copy(fp , nfp)
    ##
    fu = make_txt4_forest_tree
    tx = fu(p.root_dir , p.gitignore_file , only_dirs = True)
    print(tx)
    ##
    with open('tree.txt' , 'w') as fi :
        fi.write(tx)
    ##

    nfp.unlink()
    gs.rmdir()

    ##

##
if __name__ == "__main__" :
    main()
    print('Done!')
