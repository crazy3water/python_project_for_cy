import pandas as pd
import os


# put HCPdataset CC_2\CC_4 into MRdataset
def do_exchange_cc24(HCPdataset_sub_file_path_csv, MRdataset_sub_file_path_csv, MRdataset_result_sub_file_path_csv):
    exchange_headers = ["CC_2", "CC_4"]

    HCPdatasetPD = pd.read_csv(HCPdataset_sub_file_path_csv, sep="[;,]")
    MRdatasetPD = pd.read_csv(MRdataset_sub_file_path_csv)

    for head in exchange_headers:
        MRdatasetPD[head] = HCPdatasetPD[head]

    MRdatasetPD.to_csv(MRdataset_result_sub_file_path_csv)


if __name__ == "__main__":
    print("start")

    rootPath_HCPdataset = r'/Users/sanshui/PycharmProjects/pythonProject_cy/MCH_MR/HCPdataset'
    rootPath_MRdataset = r'/Users/sanshui/PycharmProjects/pythonProject_cy/MCH_MR/MRdataset'

    # 要求 HCPdataset中的sub文件夹名称与MRdataset对应
    HCPdataset_file_num = len(os.listdir(rootPath_HCPdataset))
    MRdataset_file_num = len(os.listdir(rootPath_HCPdataset))

    if HCPdataset_file_num != MRdataset_file_num:
        print("文件数量不一致")
    else:
        # create new MRdataset result
        rootPath_MRdataset_result = rootPath_MRdataset + "Result"
        if not os.path.exists(rootPath_MRdataset_result):
            os.mkdir(rootPath_MRdataset_result)

        for HCPdataset_sub_file in os.listdir(rootPath_HCPdataset):
            if "sub" not in HCPdataset_sub_file:
                print("出现了非sub文件名", HCPdataset_sub_file)
                continue
            # get the sub file path,
            # such as : /Users/sanshui/PycharmProjects/pythonProject_cy/MCH_MR/MRdataset/sub001
            HCPdataset_sub_file_path = os.path.join(rootPath_HCPdataset, HCPdataset_sub_file)
            MRdataset_sub_file_path = os.path.join(rootPath_MRdataset, HCPdataset_sub_file)
            MRdataset_result_sub_file_path = os.path.join(rootPath_MRdataset_result, HCPdataset_sub_file)
            # create new sub file in MRdataset result
            # such as: /Users/sanshui/PycharmProjects/pythonProject_cy/MCH_MR/MRdatasetResult/sub001
            if not os.path.exists(MRdataset_result_sub_file_path):
                os.mkdir(MRdataset_result_sub_file_path)

            # get the csv path,
            # such as : /Users/sanshui/PycharmProjects/pythonProject_cy/MCH_MR/MRdataset/sub001/Tractometry.csv
            HCPdataset_sub_file_path_csv = os.path.join(HCPdataset_sub_file_path, "Tractometry.csv")
            MRdataset_sub_file_path_csv = os.path.join(MRdataset_sub_file_path, "Tractometry.csv")
            MRdataset_result_sub_file_path_csv = os.path.join(MRdataset_result_sub_file_path, "Tractometry.csv")

            do_exchange_cc24(HCPdataset_sub_file_path_csv, MRdataset_sub_file_path_csv,
                             MRdataset_result_sub_file_path_csv)
