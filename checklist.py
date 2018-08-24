import sys, os, pyutils

def parseArgs():
    # Remove the name of the file
    sys.argv.pop(0)

    args = {}
    for tag, arg in list(pyutils.chunks(sys.argv, 2)):
        # Template directory
        if tag == '-t':
            templateDirectory = os.path.join(os.path.dirname(__file__), arg)
            args['templateDirectory'] = templateDirectory
        # Files to keep, separated by comma (no space)
        if tag == '-k':
            filesToKeep = arg.split(',')
            args['filesToKeep'] = filesToKeep
        # Zip file output directory
        if tag == '-o':
            outputDirectory = os.path.join(os.path.dirname(__file__), arg)
            args['outputDirectory'] = outputDirectory
    return args

args = parseArgs()
if not args['filesToKeep'] or not args['templateDirectory']:
    print 'Can\'t use program if you don\'t have files to keep or a template directory!'
    return
for file in args['filesToKeep']:
    status = pyutils.checkForEditsOutsideIfDef(file, os.path.join(args['templateDirectory'], file))
