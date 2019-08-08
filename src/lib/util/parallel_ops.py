###########################################################
###############    Parallel Operations    #################
###########################################################
import multiprocessing as mp
from tqdm import tqdm


def process_files(fn, file_paths, nprocesses=10, show_progress=True, desc=None):
    """process files in parallel
    Args:
        fn:         [processing function]
        file_paths: [file_path]

    Return: [processing function return]
    """
    if show_progress:
        pbar = tqdm(total=len(file_paths), ncols=100, desc=desc, dynamic_ncols=True)
    pool = mp.Pool(processes=nprocesses)
    done = 0 # number of processes done
    def _done(*x):
        nonlocal done
        done +=1
        pbar.update(done)
        
    results = [pool.map_async(fn, [f], callback=_done if show_progress else None) for f in file_paths]  # result objects
    output = [p.get()[0] for p in results]
    return output

