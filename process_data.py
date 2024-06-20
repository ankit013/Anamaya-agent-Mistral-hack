import pandas as pd
import argparse

datasets = ["DR","Irf","MultiWD","SAD","dreaddit"]

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Consolidate training/validation ortest datasets")
    parser.add_argument("--setname", type=str, help="The sets to consolidate. Train and validation as 'train' Test as 'test'")
    args = parser.parse_args()

    if args.setname == "train":
        rootpath = "/home/ec2-user/MentaLLama/MentalLLaMA/train_data/instruction_data"
        traindata = pd.DataFrame()
        valdata = pd.DataFrame()

        for dset in datasets:
            print("Fetching train and val data for:",dset)
            ## read traindata ##
            temp_train = pd.read_csv(rootpath+'/'+dset+'/'+'train.csv')
            temp_val = pd.read_csv(rootpath+'/'+dset+'/'+'val.csv')
            print("Number of records in train dataset for {} is {}".format(dset,temp_train.shape[0]))
            print("Number of records in val dataset for {} is {}".format(dset,temp_val.shape[0]))
            ### Append the data ###
            traindata = pd.concat([traindata,temp_train],axis=0)
            valdata = pd.concat([valdata,temp_val],axis=0)

        print("Total records captured for train set:",traindata.shape[0])
        print("Total records captured for val set:",valdata.shape[0])

        print("Columns in train set are:",traindata.columns.tolist())
        print("Columns in val set are:",valdata.columns.tolist())

        print("Trainset:\n",traindata.head())
        print("Valset:\n",valdata.head())

        ## Export the train and val data ##
        traindata.to_csv('/home/ec2-user/MentaLLama/MentalLLaMA/trainingdata.csv',index=False)
        valdata.to_csv('/home/ec2-user/MentaLLama/MentalLLaMA/validationdata.csv',index=False)
    elif args.setname == "test":
        rootpath = "/home/ec2-user/MentaLLama/MentalLLaMA/test_data/test_instruction"
        testdata = pd.DataFrame()

        for dset in datasets:
            print("Fetching test data for:",dset)
            ## read testdata ##
            temp_test = pd.read_csv(rootpath+'/'+dset+'.csv')
            temp_test['dataset'] = dset
            print("Number of records in test dataset for {} is {}".format(dset,temp_test.shape[0]))
            ### Append the data ###
            testdata = pd.concat([testdata,temp_test],axis=0)

        print("Total records captured for test set:",testdata.shape[0])

        print("Columns in test set are:",testdata.columns.tolist())

        print("Testset:\n",testdata.head())

        ## Export the train and val data ##
        testdata.to_csv('/home/ec2-user/MentaLLama/MentalLLaMA/testdata.csv',index=False)


