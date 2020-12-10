import os
from time import time
from multiprocessing import Process, Pipe

success = 0
fail_timeout = 0
fail_wrong = 0
total = 0
timeout = 1.5


def run_test(fname, pipe_end):
    res = os.popen("cat {} | python3 torre_dados.py".format(fname)).read()
    expected = os.popen("cat {}".format(fname.replace("in", "sol"))).read()
    pipe_end.send(res == expected)


for dirname, _, filenames in os.walk("data/"):
    for filename in filenames:
        fname = os.path.join(dirname, filename)
        if (".in") in fname:
            spl = fname.split("/")
            teste = spl[1]
            caso = spl[2].split(".")[0]
            print("Teste {}, caso {}:".format(teste, caso))
            child_conn, parent_conn = Pipe()
            test = Process(target=run_test, args=(fname, child_conn), daemon=True)
            test.start()
            start_time = time()
            res = None
            total += 1
            while (time() - start_time) < timeout:
                if parent_conn.poll():
                    res = parent_conn.recv()
                    break
            if res is None:
                print("-> Falha (timeout)\n")
                fail_timeout += 1
            elif not res:
                print("-> Falha (resultado incorreto)\n")
                fail_wrong += 1
            else:
                success += 1
                print("-> Sucesso!\n")
            test.kill()

print("Total: {}, acertos: {}, timeout: {}, errado: {}".format(total, success, fail_timeout, fail_wrong))
