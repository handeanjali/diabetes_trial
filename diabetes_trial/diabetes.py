{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3a5f4846",
   "metadata": {},
   "source": [
    "# Importing the Dependencies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1d34661b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "920fac67",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "\n",
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1a7d8af4",
   "metadata": {},
   "source": [
    "# Data Collection"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "548032e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# loading the diabetes dataset to a pandas DataFrame\n",
    "df=pd.read_csv(\"diabetes.csv\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dcb32015",
   "metadata": {},
   "source": [
    "# Exploratory Data Analysis (EDA)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a1f1a804",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>6</td>\n",
       "      <td>148</td>\n",
       "      <td>72</td>\n",
       "      <td>35</td>\n",
       "      <td>0</td>\n",
       "      <td>33.6</td>\n",
       "      <td>0.627</td>\n",
       "      <td>50</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>66</td>\n",
       "      <td>29</td>\n",
       "      <td>0</td>\n",
       "      <td>26.6</td>\n",
       "      <td>0.351</td>\n",
       "      <td>31</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8</td>\n",
       "      <td>183</td>\n",
       "      <td>64</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>23.3</td>\n",
       "      <td>0.672</td>\n",
       "      <td>32</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>89</td>\n",
       "      <td>66</td>\n",
       "      <td>23</td>\n",
       "      <td>94</td>\n",
       "      <td>28.1</td>\n",
       "      <td>0.167</td>\n",
       "      <td>21</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>137</td>\n",
       "      <td>40</td>\n",
       "      <td>35</td>\n",
       "      <td>168</td>\n",
       "      <td>43.1</td>\n",
       "      <td>2.288</td>\n",
       "      <td>33</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
       "0            6      148             72             35        0  33.6   \n",
       "1            1       85             66             29        0  26.6   \n",
       "2            8      183             64              0        0  23.3   \n",
       "3            1       89             66             23       94  28.1   \n",
       "4            0      137             40             35      168  43.1   \n",
       "\n",
       "   DiabetesPedigreeFunction  Age  Outcome  \n",
       "0                     0.627   50        1  \n",
       "1                     0.351   31        0  \n",
       "2                     0.672   32        1  \n",
       "3                     0.167   21        0  \n",
       "4                     2.288   33        1  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# printing the first five rows of the data\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1d6acbe2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>756</th>\n",
       "      <td>7</td>\n",
       "      <td>137</td>\n",
       "      <td>90</td>\n",
       "      <td>41</td>\n",
       "      <td>0</td>\n",
       "      <td>32.0</td>\n",
       "      <td>0.391</td>\n",
       "      <td>39</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>757</th>\n",
       "      <td>0</td>\n",
       "      <td>123</td>\n",
       "      <td>72</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>36.3</td>\n",
       "      <td>0.258</td>\n",
       "      <td>52</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>758</th>\n",
       "      <td>1</td>\n",
       "      <td>106</td>\n",
       "      <td>76</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>37.5</td>\n",
       "      <td>0.197</td>\n",
       "      <td>26</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>759</th>\n",
       "      <td>6</td>\n",
       "      <td>190</td>\n",
       "      <td>92</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>35.5</td>\n",
       "      <td>0.278</td>\n",
       "      <td>66</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>760</th>\n",
       "      <td>2</td>\n",
       "      <td>88</td>\n",
       "      <td>58</td>\n",
       "      <td>26</td>\n",
       "      <td>16</td>\n",
       "      <td>28.4</td>\n",
       "      <td>0.766</td>\n",
       "      <td>22</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>761</th>\n",
       "      <td>9</td>\n",
       "      <td>170</td>\n",
       "      <td>74</td>\n",
       "      <td>31</td>\n",
       "      <td>0</td>\n",
       "      <td>44.0</td>\n",
       "      <td>0.403</td>\n",
       "      <td>43</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>762</th>\n",
       "      <td>9</td>\n",
       "      <td>89</td>\n",
       "      <td>62</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>22.5</td>\n",
       "      <td>0.142</td>\n",
       "      <td>33</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>763</th>\n",
       "      <td>10</td>\n",
       "      <td>101</td>\n",
       "      <td>76</td>\n",
       "      <td>48</td>\n",
       "      <td>180</td>\n",
       "      <td>32.9</td>\n",
       "      <td>0.171</td>\n",
       "      <td>63</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>764</th>\n",
       "      <td>2</td>\n",
       "      <td>122</td>\n",
       "      <td>70</td>\n",
       "      <td>27</td>\n",
       "      <td>0</td>\n",
       "      <td>36.8</td>\n",
       "      <td>0.340</td>\n",
       "      <td>27</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>765</th>\n",
       "      <td>5</td>\n",
       "      <td>121</td>\n",
       "      <td>72</td>\n",
       "      <td>23</td>\n",
       "      <td>112</td>\n",
       "      <td>26.2</td>\n",
       "      <td>0.245</td>\n",
       "      <td>30</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>766</th>\n",
       "      <td>1</td>\n",
       "      <td>126</td>\n",
       "      <td>60</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>30.1</td>\n",
       "      <td>0.349</td>\n",
       "      <td>47</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>767</th>\n",
       "      <td>1</td>\n",
       "      <td>93</td>\n",
       "      <td>70</td>\n",
       "      <td>31</td>\n",
       "      <td>0</td>\n",
       "      <td>30.4</td>\n",
       "      <td>0.315</td>\n",
       "      <td>23</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
       "756            7      137             90             41        0  32.0   \n",
       "757            0      123             72              0        0  36.3   \n",
       "758            1      106             76              0        0  37.5   \n",
       "759            6      190             92              0        0  35.5   \n",
       "760            2       88             58             26       16  28.4   \n",
       "761            9      170             74             31        0  44.0   \n",
       "762            9       89             62              0        0  22.5   \n",
       "763           10      101             76             48      180  32.9   \n",
       "764            2      122             70             27        0  36.8   \n",
       "765            5      121             72             23      112  26.2   \n",
       "766            1      126             60              0        0  30.1   \n",
       "767            1       93             70             31        0  30.4   \n",
       "\n",
       "     DiabetesPedigreeFunction  Age  Outcome  \n",
       "756                     0.391   39        0  \n",
       "757                     0.258   52        1  \n",
       "758                     0.197   26        0  \n",
       "759                     0.278   66        1  \n",
       "760                     0.766   22        0  \n",
       "761                     0.403   43        1  \n",
       "762                     0.142   33        0  \n",
       "763                     0.171   63        0  \n",
       "764                     0.340   27        0  \n",
       "765                     0.245   30        0  \n",
       "766                     0.349   47        1  \n",
       "767                     0.315   23        0  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# printing the last five rows of the data\n",
    "df.tail(12)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2ddf80cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(768, 9)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# number of rows and columns in the dataset\n",
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "7097459f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 768 entries, 0 to 767\n",
      "Data columns (total 9 columns):\n",
      " #   Column                    Non-Null Count  Dtype  \n",
      "---  ------                    --------------  -----  \n",
      " 0   Pregnancies               768 non-null    int64  \n",
      " 1   Glucose                   768 non-null    int64  \n",
      " 2   BloodPressure             768 non-null    int64  \n",
      " 3   SkinThickness             768 non-null    int64  \n",
      " 4   Insulin                   768 non-null    int64  \n",
      " 5   BMI                       768 non-null    float64\n",
      " 6   DiabetesPedigreeFunction  768 non-null    float64\n",
      " 7   Age                       768 non-null    int64  \n",
      " 8   Outcome                   768 non-null    int64  \n",
      "dtypes: float64(2), int64(7)\n",
      "memory usage: 54.1 KB\n"
     ]
    }
   ],
   "source": [
    "# concise summary of the dataset\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2e4dd76a",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>3.845052</td>\n",
       "      <td>120.894531</td>\n",
       "      <td>69.105469</td>\n",
       "      <td>20.536458</td>\n",
       "      <td>79.799479</td>\n",
       "      <td>31.992578</td>\n",
       "      <td>0.471876</td>\n",
       "      <td>33.240885</td>\n",
       "      <td>0.348958</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>3.369578</td>\n",
       "      <td>31.972618</td>\n",
       "      <td>19.355807</td>\n",
       "      <td>15.952218</td>\n",
       "      <td>115.244002</td>\n",
       "      <td>7.884160</td>\n",
       "      <td>0.331329</td>\n",
       "      <td>11.760232</td>\n",
       "      <td>0.476951</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.078000</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>99.000000</td>\n",
       "      <td>62.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>27.300000</td>\n",
       "      <td>0.243750</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>117.000000</td>\n",
       "      <td>72.000000</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>30.500000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>0.372500</td>\n",
       "      <td>29.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>6.000000</td>\n",
       "      <td>140.250000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>127.250000</td>\n",
       "      <td>36.600000</td>\n",
       "      <td>0.626250</td>\n",
       "      <td>41.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>17.000000</td>\n",
       "      <td>199.000000</td>\n",
       "      <td>122.000000</td>\n",
       "      <td>99.000000</td>\n",
       "      <td>846.000000</td>\n",
       "      <td>67.100000</td>\n",
       "      <td>2.420000</td>\n",
       "      <td>81.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Pregnancies     Glucose  BloodPressure  SkinThickness     Insulin  \\\n",
       "count   768.000000  768.000000     768.000000     768.000000  768.000000   \n",
       "mean      3.845052  120.894531      69.105469      20.536458   79.799479   \n",
       "std       3.369578   31.972618      19.355807      15.952218  115.244002   \n",
       "min       0.000000    0.000000       0.000000       0.000000    0.000000   \n",
       "25%       1.000000   99.000000      62.000000       0.000000    0.000000   \n",
       "50%       3.000000  117.000000      72.000000      23.000000   30.500000   \n",
       "75%       6.000000  140.250000      80.000000      32.000000  127.250000   \n",
       "max      17.000000  199.000000     122.000000      99.000000  846.000000   \n",
       "\n",
       "              BMI  DiabetesPedigreeFunction         Age     Outcome  \n",
       "count  768.000000                768.000000  768.000000  768.000000  \n",
       "mean    31.992578                  0.471876   33.240885    0.348958  \n",
       "std      7.884160                  0.331329   11.760232    0.476951  \n",
       "min      0.000000                  0.078000   21.000000    0.000000  \n",
       "25%     27.300000                  0.243750   24.000000    0.000000  \n",
       "50%     32.000000                  0.372500   29.000000    0.000000  \n",
       "75%     36.600000                  0.626250   41.000000    1.000000  \n",
       "max     67.100000                  2.420000   81.000000    1.000000  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# statistical measures of the data\n",
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "60430c2b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pregnancies                 0\n",
       "Glucose                     0\n",
       "BloodPressure               0\n",
       "SkinThickness               0\n",
       "Insulin                     0\n",
       "BMI                         0\n",
       "DiabetesPedigreeFunction    0\n",
       "Age                         0\n",
       "Outcome                     0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# checking the number of null values in each column\n",
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "380f8a05",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Outcome\n",
       "0    500\n",
       "1    268\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# number of distinct values in the Outcome column of the data\n",
    "df[\"Outcome\"].value_counts()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "241a38dd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Outcome</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3.298000</td>\n",
       "      <td>109.980000</td>\n",
       "      <td>68.184000</td>\n",
       "      <td>19.664000</td>\n",
       "      <td>68.792000</td>\n",
       "      <td>30.304200</td>\n",
       "      <td>0.429734</td>\n",
       "      <td>31.190000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.865672</td>\n",
       "      <td>141.257463</td>\n",
       "      <td>70.824627</td>\n",
       "      <td>22.164179</td>\n",
       "      <td>100.335821</td>\n",
       "      <td>35.142537</td>\n",
       "      <td>0.550500</td>\n",
       "      <td>37.067164</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Pregnancies     Glucose  BloodPressure  SkinThickness     Insulin  \\\n",
       "Outcome                                                                      \n",
       "0           3.298000  109.980000      68.184000      19.664000   68.792000   \n",
       "1           4.865672  141.257463      70.824627      22.164179  100.335821   \n",
       "\n",
       "               BMI  DiabetesPedigreeFunction        Age  \n",
       "Outcome                                                  \n",
       "0        30.304200                  0.429734  31.190000  \n",
       "1        35.142537                  0.550500  37.067164  "
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# average of each column for the distinct values in Outcome column\n",
    "df.groupby(\"Outcome\").mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "59bea3b9",
   "metadata": {},
   "source": [
    "# Seperating the data and label"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "2f079c41",
   "metadata": {},
   "outputs": [],
   "source": [
    "# seperating the data and label into X and Y respectively\n",
    "X=df.iloc[:,0:8]\n",
    "Y=df[\"Outcome\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4dde7447",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(     Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
       " 0              6      148             72             35        0  33.6   \n",
       " 1              1       85             66             29        0  26.6   \n",
       " 2              8      183             64              0        0  23.3   \n",
       " 3              1       89             66             23       94  28.1   \n",
       " 4              0      137             40             35      168  43.1   \n",
       " ..           ...      ...            ...            ...      ...   ...   \n",
       " 763           10      101             76             48      180  32.9   \n",
       " 764            2      122             70             27        0  36.8   \n",
       " 765            5      121             72             23      112  26.2   \n",
       " 766            1      126             60              0        0  30.1   \n",
       " 767            1       93             70             31        0  30.4   \n",
       " \n",
       "      DiabetesPedigreeFunction  Age  \n",
       " 0                       0.627   50  \n",
       " 1                       0.351   31  \n",
       " 2                       0.672   32  \n",
       " 3                       0.167   21  \n",
       " 4                       2.288   33  \n",
       " ..                        ...  ...  \n",
       " 763                     0.171   63  \n",
       " 764                     0.340   27  \n",
       " 765                     0.245   30  \n",
       " 766                     0.349   47  \n",
       " 767                     0.315   23  \n",
       " \n",
       " [768 rows x 8 columns],\n",
       " 0      1\n",
       " 1      0\n",
       " 2      1\n",
       " 3      0\n",
       " 4      1\n",
       "       ..\n",
       " 763    0\n",
       " 764    0\n",
       " 765    0\n",
       " 766    1\n",
       " 767    0\n",
       " Name: Outcome, Length: 768, dtype: int64)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X,Y"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c720fd36",
   "metadata": {},
   "source": [
    "# Scaling the Data\n",
    "\n",
    "\n",
    "# Data Standardization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "34464d08",
   "metadata": {},
   "outputs": [],
   "source": [
    "scaler= StandardScaler()\n",
    "X = scaler.fit_transform(X)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "d76c9703",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "#Y= df['Outcome']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b3b5572d",
   "metadata": {},
   "source": [
    "# Train Test Split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "df00710b",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, stratify=Y,random_state=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "1e3ccd2f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(768, 8) (614, 8) (154, 8)\n"
     ]
    }
   ],
   "source": [
    "print(X.shape, X_train.shape, X_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "296851e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(768,) (614,) (154,)\n"
     ]
    }
   ],
   "source": [
    "print(Y.shape, Y_train.shape, Y_test.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "963018ae",
   "metadata": {},
   "source": [
    "# Model Building"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "82ba159c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model accuracy with Logistic Regression :  0.7857142857142857\n"
     ]
    }
   ],
   "source": [
    "LR  = LogisticRegression(\"l2\",random_state=42)\n",
    "\n",
    "LR.fit(X_train, Y_train)\n",
    "\n",
    "\n",
    "LR_pred = LR.predict(X_test)\n",
    "\n",
    "\n",
    "LR_accuracy = accuracy_score(Y_test, LR_pred)\n",
    "\n",
    "\n",
    "print(\"Model accuracy with Logistic Regression : \",LR_accuracy)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "1549de35",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "filename = \"diabetes.pkl\"\n",
    "with open(filename, 'wb') as file:\n",
    "    pickle.dump(LR, file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68441dfd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
