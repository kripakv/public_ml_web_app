{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "056e385f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "67e84971",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: textblob_fr in c:\\users\\kripa\\anaconda3\\lib\\site-packages (0.2.0)"
     ]
    }
   ],
   "source": [
    "!pip install textblob_fr "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "1d5efb0c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Requirement already satisfied: textblob>=0.8.0 in c:\\users\\kripa\\anaconda3\\lib\\site-packages (from textblob_fr) (0.17.1)\n",
      "Requirement already satisfied: nltk>=3.1 in c:\\users\\kripa\\anaconda3\\lib\\site-packages (from textblob>=0.8.0->textblob_fr) (3.6.5)\n",
      "Requirement already satisfied: click in c:\\users\\kripa\\anaconda3\\lib\\site-packages (from nltk>=3.1->textblob>=0.8.0->textblob_fr) (8.0.3)\n",
      "Requirement already satisfied: joblib in c:\\users\\kripa\\anaconda3\\lib\\site-packages (from nltk>=3.1->textblob>=0.8.0->textblob_fr) (1.1.0)\n",
      "Requirement already satisfied: regex>=2021.8.3 in c:\\users\\kripa\\anaconda3\\lib\\site-packages (from nltk>=3.1->textblob>=0.8.0->textblob_fr) (2021.8.3)\n",
      "Requirement already satisfied: tqdm in c:\\users\\kripa\\anaconda3\\lib\\site-packages (from nltk>=3.1->textblob>=0.8.0->textblob_fr) (4.62.3)\n",
      "Requirement already satisfied: colorama in c:\\users\\kripa\\anaconda3\\lib\\site-packages (from click->nltk>=3.1->textblob>=0.8.0->textblob_fr) (0.4.4)\n"
     ]
    }
   ],
   "source": [
    "from nltk.tokenize import sent_tokenize\n",
    "from nltk.tokenize import word_tokenize\n",
    "import re\n",
    "import string\n",
    "from textblob import TextBlob\n",
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "8d852d3c",
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
       "      <th>ID</th>\n",
       "      <th>Review URL</th>\n",
       "      <th>Text</th>\n",
       "      <th>Star</th>\n",
       "      <th>Thumbs Up</th>\n",
       "      <th>User Name</th>\n",
       "      <th>Developer Reply</th>\n",
       "      <th>Version</th>\n",
       "      <th>Review Date</th>\n",
       "      <th>App ID</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3886</td>\n",
       "      <td>https://play.google.com/store/apps/details?id=...</td>\n",
       "      <td>This is very helpfull aap.</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>INDIAN Knowledge</td>\n",
       "      <td>NaN</td>\n",
       "      <td>83.0.4103.106</td>\n",
       "      <td>2020-12-19</td>\n",
       "      <td>com.android.chrome</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3887</td>\n",
       "      <td>https://play.google.com/store/apps/details?id=...</td>\n",
       "      <td>Good</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>Ijeoma Happiness</td>\n",
       "      <td>NaN</td>\n",
       "      <td>85.0.4183.127</td>\n",
       "      <td>2020-12-19</td>\n",
       "      <td>com.android.chrome</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3888</td>\n",
       "      <td>https://play.google.com/store/apps/details?id=...</td>\n",
       "      <td>Not able to update. Neither able to uninstall.</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Priti D BtCFs-29</td>\n",
       "      <td>NaN</td>\n",
       "      <td>85.0.4183.127</td>\n",
       "      <td>2020-12-19</td>\n",
       "      <td>com.android.chrome</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3889</td>\n",
       "      <td>https://play.google.com/store/apps/details?id=...</td>\n",
       "      <td>Nice app</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>Ajeet Raja</td>\n",
       "      <td>NaN</td>\n",
       "      <td>77.0.3865.116</td>\n",
       "      <td>2020-12-19</td>\n",
       "      <td>com.android.chrome</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3890</td>\n",
       "      <td>https://play.google.com/store/apps/details?id=...</td>\n",
       "      <td>Many unwanted ads</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Rams Mp</td>\n",
       "      <td>NaN</td>\n",
       "      <td>87.0.4280.66</td>\n",
       "      <td>2020-12-19</td>\n",
       "      <td>com.android.chrome</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     ID                                         Review URL  \\\n",
       "0  3886  https://play.google.com/store/apps/details?id=...   \n",
       "1  3887  https://play.google.com/store/apps/details?id=...   \n",
       "2  3888  https://play.google.com/store/apps/details?id=...   \n",
       "3  3889  https://play.google.com/store/apps/details?id=...   \n",
       "4  3890  https://play.google.com/store/apps/details?id=...   \n",
       "\n",
       "                                             Text  Star  Thumbs Up  \\\n",
       "0                      This is very helpfull aap.     5          0   \n",
       "1                                            Good     3          2   \n",
       "2  Not able to update. Neither able to uninstall.     1          0   \n",
       "3                                        Nice app     4          0   \n",
       "4                               Many unwanted ads     1          0   \n",
       "\n",
       "          User Name Developer Reply        Version Review Date  \\\n",
       "0  INDIAN Knowledge             NaN  83.0.4103.106  2020-12-19   \n",
       "1  Ijeoma Happiness             NaN  85.0.4183.127  2020-12-19   \n",
       "2  Priti D BtCFs-29             NaN  85.0.4183.127  2020-12-19   \n",
       "3        Ajeet Raja             NaN  77.0.3865.116  2020-12-19   \n",
       "4           Rams Mp             NaN   87.0.4280.66  2020-12-19   \n",
       "\n",
       "               App ID  \n",
       "0  com.android.chrome  \n",
       "1  com.android.chrome  \n",
       "2  com.android.chrome  \n",
       "3  com.android.chrome  \n",
       "4  com.android.chrome  "
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = pd.read_csv('C:/chrome_reviews.csv')\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "00be3765",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(7204, 10)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "432c41c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['ID', 'Review URL', 'Text', 'Star', 'Thumbs Up', 'User Name',\n",
       "       'Developer Reply', 'Version', 'Review Date', 'App ID'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "73fb4dfc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "ID                    0\n",
       "Review URL            0\n",
       "Text                  1\n",
       "Star                  0\n",
       "Thumbs Up             0\n",
       "User Name             0\n",
       "Developer Reply    7109\n",
       "Version              85\n",
       "Review Date           0\n",
       "App ID                0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "6a2d4ad4",
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
       "      <th>ID</th>\n",
       "      <th>Text</th>\n",
       "      <th>Star</th>\n",
       "      <th>Thumbs Up</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3886</td>\n",
       "      <td>This is very helpfull aap.</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3887</td>\n",
       "      <td>Good</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3888</td>\n",
       "      <td>Not able to update. Neither able to uninstall.</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3889</td>\n",
       "      <td>Nice app</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3890</td>\n",
       "      <td>Many unwanted ads</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     ID                                            Text  Star  Thumbs Up\n",
       "0  3886                      This is very helpfull aap.     5          0\n",
       "1  3887                                            Good     3          2\n",
       "2  3888  Not able to update. Neither able to uninstall.     1          0\n",
       "3  3889                                        Nice app     4          0\n",
       "4  3890                               Many unwanted ads     1          0"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data= data.drop(['User Name'],axis=1)\n",
    "data= data.drop(['Developer Reply'],axis=1)\n",
    "data= data.drop(['Version'],axis=1)\n",
    "data= data.drop(['Review URL'],axis=1)\n",
    "data= data.drop(['Review Date'],axis=1)\n",
    "data= data.drop(['App ID'],axis=1)\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "cc34acd1",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "data.dropna(inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "3482b05a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "ID           0\n",
       "Text         0\n",
       "Star         0\n",
       "Thumbs Up    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "2eaf029a",
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
       "      <th>ID</th>\n",
       "      <th>Text</th>\n",
       "      <th>Star</th>\n",
       "      <th>Thumbs Up</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3886</td>\n",
       "      <td>This is very helpfull aap.</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3887</td>\n",
       "      <td>Good</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3888</td>\n",
       "      <td>Not able to update. Neither able to uninstall.</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3889</td>\n",
       "      <td>Nice app</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3890</td>\n",
       "      <td>Many unwanted ads</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>3891</td>\n",
       "      <td>This app good</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>3892</td>\n",
       "      <td>Yes yes</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>3893</td>\n",
       "      <td>Awesome</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>3894</td>\n",
       "      <td>Very bad app 😞</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>3895</td>\n",
       "      <td>Many times I tried to update its not updating....</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     ID                                               Text  Star  Thumbs Up\n",
       "0  3886                         This is very helpfull aap.     5          0\n",
       "1  3887                                               Good     3          2\n",
       "2  3888     Not able to update. Neither able to uninstall.     1          0\n",
       "3  3889                                           Nice app     4          0\n",
       "4  3890                                  Many unwanted ads     1          0\n",
       "5  3891                                      This app good     4          0\n",
       "6  3892                                            Yes yes     5          0\n",
       "7  3893                                            Awesome     5          0\n",
       "8  3894                                     Very bad app 😞     1          0\n",
       "9  3895  Many times I tried to update its not updating....     1          0"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "1098d771",
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
       "      <th>ID</th>\n",
       "      <th>Text</th>\n",
       "      <th>Star</th>\n",
       "      <th>Thumbs Up</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3888</td>\n",
       "      <td>Not able to update. Neither able to uninstall.</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3890</td>\n",
       "      <td>Many unwanted ads</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>3894</td>\n",
       "      <td>Very bad app 😞</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>3895</td>\n",
       "      <td>Many times I tried to update its not updating....</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>3898</td>\n",
       "      <td>App is not getting update and it is not gettin...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      ID                                               Text  Star  Thumbs Up\n",
       "2   3888     Not able to update. Neither able to uninstall.     1          0\n",
       "4   3890                                  Many unwanted ads     1          0\n",
       "8   3894                                     Very bad app 😞     1          0\n",
       "9   3895  Many times I tried to update its not updating....     1          0\n",
       "12  3898  App is not getting update and it is not gettin...     1          0"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = data[data.Star != 5]\n",
    "data = data[data.Star != 4]\n",
    "data = data[data.Star != 3]\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "66f8b87b",
   "metadata": {},
   "outputs": [],
   "source": [
    "senti_list = []\n",
    "for i in data[\"Text\"]:\n",
    "    score = TextBlob(i).sentiment[0]\n",
    "    if (score > 0):\n",
    "        senti_list.append('Positive')\n",
    "    elif (score < 0):\n",
    "        senti_list.append('Negative')\n",
    "    else:\n",
    "        senti_list.append('Neutral') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "1a1ce2ea",
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
       "      <th>ID</th>\n",
       "      <th>Text</th>\n",
       "      <th>Star</th>\n",
       "      <th>Thumbs Up</th>\n",
       "      <th>sentiment</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3888</td>\n",
       "      <td>Not able to update. Neither able to uninstall.</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3890</td>\n",
       "      <td>Many unwanted ads</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>3894</td>\n",
       "      <td>Very bad app 😞</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Negative</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>3895</td>\n",
       "      <td>Many times I tried to update its not updating....</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>3898</td>\n",
       "      <td>App is not getting update and it is not gettin...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      ID                                               Text  Star  Thumbs Up  \\\n",
       "2   3888     Not able to update. Neither able to uninstall.     1          0   \n",
       "4   3890                                  Many unwanted ads     1          0   \n",
       "8   3894                                     Very bad app 😞     1          0   \n",
       "9   3895  Many times I tried to update its not updating....     1          0   \n",
       "12  3898  App is not getting update and it is not gettin...     1          0   \n",
       "\n",
       "   sentiment  \n",
       "2   Positive  \n",
       "4   Positive  \n",
       "8   Negative  \n",
       "9   Positive  \n",
       "12  Positive  "
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[\"sentiment\"]=senti_list\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "2574cabf",
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
       "      <th>ID</th>\n",
       "      <th>Text</th>\n",
       "      <th>Star</th>\n",
       "      <th>Thumbs Up</th>\n",
       "      <th>sentiment</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3888</td>\n",
       "      <td>Not able to update. Neither able to uninstall.</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3890</td>\n",
       "      <td>Many unwanted ads</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>3895</td>\n",
       "      <td>Many times I tried to update its not updating....</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>3898</td>\n",
       "      <td>App is not getting update and it is not gettin...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>3901</td>\n",
       "      <td>Very coming in real status. Thank you</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>3905</td>\n",
       "      <td>I want to download greana free fire but that n...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>42</th>\n",
       "      <td>3928</td>\n",
       "      <td>Okk kind but bad then brave</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48</th>\n",
       "      <td>3934</td>\n",
       "      <td>Unable to update won't load crashing at times ...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>59</th>\n",
       "      <td>3945</td>\n",
       "      <td>Don't know why chrome started controlling the ...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>80</th>\n",
       "      <td>3966</td>\n",
       "      <td>I am facing a serious problem with my Google C...</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      ID                                               Text  Star  Thumbs Up  \\\n",
       "2   3888     Not able to update. Neither able to uninstall.     1          0   \n",
       "4   3890                                  Many unwanted ads     1          0   \n",
       "9   3895  Many times I tried to update its not updating....     1          0   \n",
       "12  3898  App is not getting update and it is not gettin...     1          0   \n",
       "15  3901              Very coming in real status. Thank you     1          0   \n",
       "19  3905  I want to download greana free fire but that n...     1          0   \n",
       "42  3928                        Okk kind but bad then brave     1          0   \n",
       "48  3934  Unable to update won't load crashing at times ...     1          0   \n",
       "59  3945  Don't know why chrome started controlling the ...     1          0   \n",
       "80  3966  I am facing a serious problem with my Google C...     2          0   \n",
       "\n",
       "   sentiment  \n",
       "2   Positive  \n",
       "4   Positive  \n",
       "9   Positive  \n",
       "12  Positive  \n",
       "15  Positive  \n",
       "19  Positive  \n",
       "42  Positive  \n",
       "48  Positive  \n",
       "59  Positive  \n",
       "80  Positive  "
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = data[data.sentiment == 'Positive']\n",
    "data.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "15e55267",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.to_csv(r'C:\\Users\\kripa\\OneDrive\\Documents\\datanew.csv',index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d8f965d8",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
