#!/usr/bin/env python
'''
This will eventually get replaced with Require.js
but until then it's a quick hack to save time.
'''

import os

EXIT_SUCCESS = 0


def precompile(compiler='handlebars'):
    '''
    Quick hack to precompile all templates
    '''
    success = 0
    print("[*] Precompiling templates, please wait ...")
    files = filter(lambda f: f.endswith('.handlebars'), os.listdir('.'))
    for hb in files:
        output = ''.join(hb.split('.')[:-1]) + '.js'
        exit_status = os.system('%s %s -f ../js/%s' % (
            compiler, hb, output
        ))
        if exit_status == EXIT_SUCCESS:
            print("[$] Successfully compiled %s" % hb)
            success += 1
        else:
            print("[!] Failed to compile %s" % hb)
    print("[*] Successfully compiled %d of %d templates" % (
        success, len(files)
    ))
    if success == len(files):
        minify()


def minify(minifier='minify', output='templates.min.js'):
    print("[*] Minifying JavaScript files ...")
    os.chdir("../js")
    files = filter(lambda f: f.endswith('.js'), os.listdir('.'))
    os.system("%s %s > ./%s" % (minifier, " ".join(files), output))
    os.system("rm %s" % " ".join(files))


if __name__ == '__main__':
    precompile()
