import dicom
import os
import sys

if __name__ == '__main__':
    #PathDicom = "/trainingData"
    PathDicom = sys.argv[1]
    for filename in os.listdir(PathDicom):
        if ".dcm" in filename.lower():
            sys.stdout.write("{}: ".format(filename))
            RefDs = dicom.read_file(os.path.join(PathDicom,filename))
            # RefDs.dir has lots of info
            print(RefDs.dir)
            firsttime=True
            sys.stdout.write('file size (MB): {}, '.format(os.path.getsize(PathDicom+"/"+filename)/1024000))
            for label in ['PatientID', 'StudyDate', 'PatientAge', 'SeriesDescription', 'Rows', 'Columns']:
                if (firsttime):
                    firsttime=False
                else:
                    sys.stdout.write(', ')
                sys.stdout.write("{}: {}".format(label, RefDs.data_element(label).value))
            print("")
