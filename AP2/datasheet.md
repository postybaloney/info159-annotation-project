# Datasheet

## Motivation

The dataset was created for use as part of the Annotation Project for INFO159: Natural Language Processing taught at UC Berkeley Spring 2026. It was created to identify the presence of certain logical fallacies found in the policy statements of the United States House of Representatives (HORs) at the time of February 2026. Parth Desai alongside Beatrice Lowman created the dataset for use in the class. There is no funding attached to the dataset creation.  

## Composition

Instances comprise of a singular policy statement from a member of the HOR. The data format is text with special characters intermixed. An example can be found at [SAMPLE](https://github.com/postybaloney/info159-annotation-project/AP2/sample.txt). There are a total of 1,330 policy statements that are in the [CSV](https://github.com/postybaloney/info159-annotation-project/AP1/issue_df.csv). There are 850 policy statements from Democrats and 580 policy statements from Republicans. It does not contain all possible policy statements as statements with length less than 110 characters were excluded as they were found to be solely comprised of placeholder text and statements that had a different format in the HTML than mentioned in the [Python Notebook](https://github.com/postybaloney/info159-annotation-project/AP1/all_issue.ipynb) were also excluded as exploration, not generalization was the basis of the creation of the dataset. Besides these exclusions, the dataset is representative of policy statements made by members of the US HOR. There is no label or target associated with the current dataset. The task of the project will lead to the instances being labeled with one or more classes, as described in the [Description](https://github.com/postybaloney/info159-annotation-project/AP2/description.md) file. There are no explicit mentions of relationships between instances and no data split is recommended at this time (March 2026). The only errors that exist are characters not understood by human readers (e.g. donâ€™t represents don't). The dataset provides a link to where the policy statement is found. There is no archival version of the link and no guarantee the link will be available forever. There are no restrictions to access the links. There is no confidential data, however, the politician who is saying the policy statement is explicitly mentioned. The data viewed directly does not cause anxiety. It identifies politicians by which side of the two-party system they belong to. It also inherently conveys political beliefs of these members of the US HOR.

## Collection Process

The entire data collection process is located in the Python Notebook labeled [all_issue.ipynb](https://github.com/postybaloney/info159-annotation-project/AP1/all_issue.ipynb). The sampling was done deterministically. Parth Desai was directly involved in the collection process and was not compensated for his time. The dataset was created in one 60 minute session of running the file in its entirety. No IRB was consulted. The data was obtained from 3rd-party sources, namely https://www.house.gov/representatives and the politicians own websites. The politicians were not notified nor consented to this data being collected. No data protection impact analysis has been done.  

## Preprocessing/Cleaning/Labeling

Removal of instances below 110 characters was done. The "raw" dataset was not preserved due to it not being relevant to the scope of the Annotation Project. The file for the creation of the dataset is labeled [all_issue.ipynb](https://github.com/postybaloney/info159-annotation-project/AP1/all_issue.ipynb).

## Uses

The dataset has not been used for a task (March 2026). The repository can be found at https://github.com/postybaloney/info159-annotation-project. The dataset could be used for any task involving the policy statements of the members of the US HOR. There is nothing that the author can presently think of that would impact future uses. Any task involving prediction of political alignment should not be using this dataset in its training.

## Distribution

The dataset will not be explicitly distributed but will exist on GitHub at https://github.com/postybaloney/info159-annotation-project with a MIT License and without a DOI. No regulatory restrictions apply to the dataset.

## Maintenance

There will be no support for the dataset following May 2026. The owner can be contacted at [parhtrudesai@gmail.com](mailto:parthrudesai@gmail.com). There is no erratum and the dataset will not be updated beyond adding annotation labels in March and April of 2026. The people in question have no clue about the retention of their information and the information will be retained indefinitely. There will only exist one version of the dataset. If one wants to build upon this work, they are more than welcome to fork the repository and conduct their work.
