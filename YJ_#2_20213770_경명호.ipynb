{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "cd7570d5",
   "metadata": {},
   "source": [
    "# 목표 : 어떤 속성이 제주 방문인구 수에 영향을 끼치는 지 분석하고  2019~2020년 방문인구수 예측하기.\n",
    "# 설명 동영상 링크 => https://youtu.be/G2ZmZniMBnY"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "40dbc0ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "#자료 출처 https://www.jejudatahub.net/data/view/data/753 제주 데이터허브\n",
    "jeju = pd.read_csv('jeju_data.csv',encoding='euc-kr')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f4603d64",
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
       "      <th>일자</th>\n",
       "      <th>시도명</th>\n",
       "      <th>읍면동명</th>\n",
       "      <th>거주인구</th>\n",
       "      <th>근무인구</th>\n",
       "      <th>방문인구</th>\n",
       "      <th>총 유동인구</th>\n",
       "      <th>교통량</th>\n",
       "      <th>평균 속도</th>\n",
       "      <th>평균 소요 시간</th>\n",
       "      <th>평균 기온</th>\n",
       "      <th>일강수량</th>\n",
       "      <th>평균 풍속</th>\n",
       "      <th>데이터기준일자</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2018-01-01</td>\n",
       "      <td>서귀포시</td>\n",
       "      <td>남원읍</td>\n",
       "      <td>291408.897</td>\n",
       "      <td>18744.131</td>\n",
       "      <td>219588.857</td>\n",
       "      <td>529741.884</td>\n",
       "      <td>76.200</td>\n",
       "      <td>53.000</td>\n",
       "      <td>40.571</td>\n",
       "      <td>2.350</td>\n",
       "      <td>0.0</td>\n",
       "      <td>3.325</td>\n",
       "      <td>2020-12-15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2018-01-01</td>\n",
       "      <td>서귀포시</td>\n",
       "      <td>대륜동</td>\n",
       "      <td>267671.778</td>\n",
       "      <td>20177.907</td>\n",
       "      <td>212778.579</td>\n",
       "      <td>500628.264</td>\n",
       "      <td>0.000</td>\n",
       "      <td>39.185</td>\n",
       "      <td>33.630</td>\n",
       "      <td>4.900</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.900</td>\n",
       "      <td>2020-12-15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2018-01-01</td>\n",
       "      <td>서귀포시</td>\n",
       "      <td>대정읍</td>\n",
       "      <td>385419.306</td>\n",
       "      <td>16536.359</td>\n",
       "      <td>161422.712</td>\n",
       "      <td>563378.377</td>\n",
       "      <td>394.789</td>\n",
       "      <td>54.632</td>\n",
       "      <td>42.579</td>\n",
       "      <td>6.633</td>\n",
       "      <td>0.0</td>\n",
       "      <td>6.367</td>\n",
       "      <td>2020-12-15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2018-01-01</td>\n",
       "      <td>서귀포시</td>\n",
       "      <td>대천동</td>\n",
       "      <td>155036.925</td>\n",
       "      <td>9403.969</td>\n",
       "      <td>150882.409</td>\n",
       "      <td>315323.303</td>\n",
       "      <td>0.000</td>\n",
       "      <td>41.583</td>\n",
       "      <td>14.375</td>\n",
       "      <td>5.100</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.300</td>\n",
       "      <td>2020-12-15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2018-01-01</td>\n",
       "      <td>서귀포시</td>\n",
       "      <td>동홍동</td>\n",
       "      <td>372744.391</td>\n",
       "      <td>26351.698</td>\n",
       "      <td>160768.257</td>\n",
       "      <td>559864.346</td>\n",
       "      <td>0.000</td>\n",
       "      <td>39.667</td>\n",
       "      <td>30.476</td>\n",
       "      <td>4.900</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.900</td>\n",
       "      <td>2020-12-15</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           일자   시도명 읍면동명        거주인구       근무인구        방문인구      총 유동인구  \\\n",
       "0  2018-01-01  서귀포시  남원읍  291408.897  18744.131  219588.857  529741.884   \n",
       "1  2018-01-01  서귀포시  대륜동  267671.778  20177.907  212778.579  500628.264   \n",
       "2  2018-01-01  서귀포시  대정읍  385419.306  16536.359  161422.712  563378.377   \n",
       "3  2018-01-01  서귀포시  대천동  155036.925   9403.969  150882.409  315323.303   \n",
       "4  2018-01-01  서귀포시  동홍동  372744.391  26351.698  160768.257  559864.346   \n",
       "\n",
       "       교통량   평균 속도  평균 소요 시간  평균 기온  일강수량  평균 풍속     데이터기준일자  \n",
       "0   76.200  53.000    40.571  2.350   0.0  3.325  2020-12-15  \n",
       "1    0.000  39.185    33.630  4.900   0.0  1.900  2020-12-15  \n",
       "2  394.789  54.632    42.579  6.633   0.0  6.367  2020-12-15  \n",
       "3    0.000  41.583    14.375  5.100   0.0  2.300  2020-12-15  \n",
       "4    0.000  39.667    30.476  4.900   0.0  1.900  2020-12-15  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "jeju.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "94fb8ef9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#데이터 확인"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "86de2097",
   "metadata": {},
   "outputs": [],
   "source": [
    "#글씨체 선택\n",
    "from matplotlib import font_manager, rc\n",
    "font_path = \"C:/Windows/Fonts/NGULIM.TTF\"\n",
    "font = font_manager.FontProperties(fname=font_path).get_name()\n",
    "rc('font', family=font)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "29e52f50",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "jeju['방문인구'].hist(bins=100)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cced409d",
   "metadata": {},
   "source": [
    "# 본 데이터는 일자, 지역별로 세세히 데이터가 나눠저 있어 통일성을 위해 일자별로 데이터의 평균값을 구해 시도하였습니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "32f13626",
   "metadata": {},
   "outputs": [],
   "source": [
    "jeju_mean=jeju.groupby(['일자'], as_index=False).mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "03426c52",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 180000 ~ 220000 사이 데이터가 가장 많다.\n",
    "jeju_mean['방문인구'].hist(bins=100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "874b7659",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "2f16dcfb",
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
       "      <th>일자</th>\n",
       "      <th>거주인구</th>\n",
       "      <th>근무인구</th>\n",
       "      <th>방문인구</th>\n",
       "      <th>총 유동인구</th>\n",
       "      <th>교통량</th>\n",
       "      <th>평균 속도</th>\n",
       "      <th>평균 소요 시간</th>\n",
       "      <th>평균 기온</th>\n",
       "      <th>일강수량</th>\n",
       "      <th>평균 풍속</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2018-01-01</td>\n",
       "      <td>317309.342098</td>\n",
       "      <td>22614.753707</td>\n",
       "      <td>198800.837073</td>\n",
       "      <td>538724.932927</td>\n",
       "      <td>289.730488</td>\n",
       "      <td>41.819561</td>\n",
       "      <td>34.339293</td>\n",
       "      <td>3.105512</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.661805</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2018-01-02</td>\n",
       "      <td>316696.629488</td>\n",
       "      <td>37324.649829</td>\n",
       "      <td>182846.761927</td>\n",
       "      <td>536868.041341</td>\n",
       "      <td>368.399268</td>\n",
       "      <td>40.727439</td>\n",
       "      <td>36.143439</td>\n",
       "      <td>4.321146</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.128049</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2018-01-03</td>\n",
       "      <td>315537.570146</td>\n",
       "      <td>37350.654659</td>\n",
       "      <td>183220.805780</td>\n",
       "      <td>536109.030707</td>\n",
       "      <td>372.731073</td>\n",
       "      <td>40.526927</td>\n",
       "      <td>36.202805</td>\n",
       "      <td>3.508317</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.984585</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2018-01-04</td>\n",
       "      <td>304965.323488</td>\n",
       "      <td>36979.035098</td>\n",
       "      <td>189812.450537</td>\n",
       "      <td>531756.809049</td>\n",
       "      <td>370.993512</td>\n",
       "      <td>40.265561</td>\n",
       "      <td>36.650073</td>\n",
       "      <td>2.739195</td>\n",
       "      <td>2.040683</td>\n",
       "      <td>2.270756</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2018-01-05</td>\n",
       "      <td>312561.529732</td>\n",
       "      <td>35778.820512</td>\n",
       "      <td>184950.181756</td>\n",
       "      <td>533290.531878</td>\n",
       "      <td>372.141561</td>\n",
       "      <td>40.186854</td>\n",
       "      <td>36.662341</td>\n",
       "      <td>2.639220</td>\n",
       "      <td>3.528463</td>\n",
       "      <td>3.083561</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>797</th>\n",
       "      <td>2020-04-25</td>\n",
       "      <td>344968.125425</td>\n",
       "      <td>23491.301075</td>\n",
       "      <td>182326.690400</td>\n",
       "      <td>550786.116825</td>\n",
       "      <td>358.247600</td>\n",
       "      <td>42.714600</td>\n",
       "      <td>36.810500</td>\n",
       "      <td>14.674425</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>4.873875</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>798</th>\n",
       "      <td>2020-04-26</td>\n",
       "      <td>343974.590175</td>\n",
       "      <td>20073.036100</td>\n",
       "      <td>170438.111975</td>\n",
       "      <td>534485.738275</td>\n",
       "      <td>315.821225</td>\n",
       "      <td>43.312775</td>\n",
       "      <td>35.853450</td>\n",
       "      <td>11.697625</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.327325</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>799</th>\n",
       "      <td>2020-04-27</td>\n",
       "      <td>336830.456275</td>\n",
       "      <td>30541.056950</td>\n",
       "      <td>164695.766500</td>\n",
       "      <td>532067.279725</td>\n",
       "      <td>384.062400</td>\n",
       "      <td>42.255300</td>\n",
       "      <td>37.553325</td>\n",
       "      <td>11.523175</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.469575</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>800</th>\n",
       "      <td>2020-04-28</td>\n",
       "      <td>334859.593525</td>\n",
       "      <td>30908.123525</td>\n",
       "      <td>167095.192925</td>\n",
       "      <td>532862.909975</td>\n",
       "      <td>398.063775</td>\n",
       "      <td>42.023025</td>\n",
       "      <td>37.564050</td>\n",
       "      <td>11.731375</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.528525</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>801</th>\n",
       "      <td>2020-04-29</td>\n",
       "      <td>331464.990975</td>\n",
       "      <td>30825.681950</td>\n",
       "      <td>174839.570300</td>\n",
       "      <td>537130.243300</td>\n",
       "      <td>413.015175</td>\n",
       "      <td>41.640900</td>\n",
       "      <td>37.710325</td>\n",
       "      <td>12.766275</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.125200</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>802 rows × 11 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             일자           거주인구          근무인구           방문인구         총 유동인구  \\\n",
       "0    2018-01-01  317309.342098  22614.753707  198800.837073  538724.932927   \n",
       "1    2018-01-02  316696.629488  37324.649829  182846.761927  536868.041341   \n",
       "2    2018-01-03  315537.570146  37350.654659  183220.805780  536109.030707   \n",
       "3    2018-01-04  304965.323488  36979.035098  189812.450537  531756.809049   \n",
       "4    2018-01-05  312561.529732  35778.820512  184950.181756  533290.531878   \n",
       "..          ...            ...           ...            ...            ...   \n",
       "797  2020-04-25  344968.125425  23491.301075  182326.690400  550786.116825   \n",
       "798  2020-04-26  343974.590175  20073.036100  170438.111975  534485.738275   \n",
       "799  2020-04-27  336830.456275  30541.056950  164695.766500  532067.279725   \n",
       "800  2020-04-28  334859.593525  30908.123525  167095.192925  532862.909975   \n",
       "801  2020-04-29  331464.990975  30825.681950  174839.570300  537130.243300   \n",
       "\n",
       "            교통량      평균 속도   평균 소요 시간      평균 기온      일강수량     평균 풍속  \n",
       "0    289.730488  41.819561  34.339293   3.105512  0.000000  2.661805  \n",
       "1    368.399268  40.727439  36.143439   4.321146  0.000000  2.128049  \n",
       "2    372.731073  40.526927  36.202805   3.508317  0.000000  2.984585  \n",
       "3    370.993512  40.265561  36.650073   2.739195  2.040683  2.270756  \n",
       "4    372.141561  40.186854  36.662341   2.639220  3.528463  3.083561  \n",
       "..          ...        ...        ...        ...       ...       ...  \n",
       "797  358.247600  42.714600  36.810500  14.674425  0.000000  4.873875  \n",
       "798  315.821225  43.312775  35.853450  11.697625  0.000000  2.327325  \n",
       "799  384.062400  42.255300  37.553325  11.523175  0.000000  2.469575  \n",
       "800  398.063775  42.023025  37.564050  11.731375  0.000000  2.528525  \n",
       "801  413.015175  41.640900  37.710325  12.766275  0.000000  2.125200  \n",
       "\n",
       "[802 rows x 11 columns]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "jeju_mean.head(-1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e02a9616",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "6a28f868",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(jeju_mean['일자'],jeju_mean['방문인구'],alpha=0.4)\n",
    "plt.xlabel('일자')\n",
    "plt.ylabel('방문인구')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "95760dfd",
   "metadata": {},
   "source": [
    "## 계절 별로 큰 의미성을 보이지 않는 것 같지만 최근으로 갈 때 방문 인구 수가 확 줄어드는걸 볼 수 있음."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "0fd5c1e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 혹시 기온에 따라 분포도가 다를까 싶어 봤지만 대체적으로 고르 분포되어 있음.\n",
    "plt.scatter(jeju_mean['평균 기온'],jeju_mean['방문인구'],alpha=0.4)\n",
    "plt.xlabel('평균 기온')\n",
    "plt.ylabel('방문인구')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c66ce848",
   "metadata": {},
   "source": [
    "# 최근으로 갈 수록 방문 인구 수가 줄어든 것으로 보아 코로나가 관련된 것이라고 생각. 코로나 일별 총 확진자 수를 대입해 보기로 함. 출처(https://coronaboard.kr/)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "bb678521",
   "metadata": {},
   "outputs": [],
   "source": [
    "corona = pd.read_csv('kr_daily.csv',encoding='euc-kr')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "1b45a892",
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
       "      <th>일자</th>\n",
       "      <th>거주인구</th>\n",
       "      <th>근무인구</th>\n",
       "      <th>방문인구</th>\n",
       "      <th>총 유동인구</th>\n",
       "      <th>교통량</th>\n",
       "      <th>평균 속도</th>\n",
       "      <th>평균 소요 시간</th>\n",
       "      <th>평균 기온</th>\n",
       "      <th>일강수량</th>\n",
       "      <th>평균 풍속</th>\n",
       "      <th>confirmed</th>\n",
       "      <th>death</th>\n",
       "      <th>released</th>\n",
       "      <th>tested</th>\n",
       "      <th>negative</th>\n",
       "      <th>daily</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2018-01-01</td>\n",
       "      <td>317309.342098</td>\n",
       "      <td>22614.753707</td>\n",
       "      <td>198800.837073</td>\n",
       "      <td>538724.932927</td>\n",
       "      <td>289.730488</td>\n",
       "      <td>41.819561</td>\n",
       "      <td>34.339293</td>\n",
       "      <td>3.105512</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.661805</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2018-01-02</td>\n",
       "      <td>316696.629488</td>\n",
       "      <td>37324.649829</td>\n",
       "      <td>182846.761927</td>\n",
       "      <td>536868.041341</td>\n",
       "      <td>368.399268</td>\n",
       "      <td>40.727439</td>\n",
       "      <td>36.143439</td>\n",
       "      <td>4.321146</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.128049</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2018-01-03</td>\n",
       "      <td>315537.570146</td>\n",
       "      <td>37350.654659</td>\n",
       "      <td>183220.805780</td>\n",
       "      <td>536109.030707</td>\n",
       "      <td>372.731073</td>\n",
       "      <td>40.526927</td>\n",
       "      <td>36.202805</td>\n",
       "      <td>3.508317</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.984585</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2018-01-04</td>\n",
       "      <td>304965.323488</td>\n",
       "      <td>36979.035098</td>\n",
       "      <td>189812.450537</td>\n",
       "      <td>531756.809049</td>\n",
       "      <td>370.993512</td>\n",
       "      <td>40.265561</td>\n",
       "      <td>36.650073</td>\n",
       "      <td>2.739195</td>\n",
       "      <td>2.040683</td>\n",
       "      <td>2.270756</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2018-01-05</td>\n",
       "      <td>312561.529732</td>\n",
       "      <td>35778.820512</td>\n",
       "      <td>184950.181756</td>\n",
       "      <td>533290.531878</td>\n",
       "      <td>372.141561</td>\n",
       "      <td>40.186854</td>\n",
       "      <td>36.662341</td>\n",
       "      <td>2.639220</td>\n",
       "      <td>3.528463</td>\n",
       "      <td>3.083561</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           일자           거주인구          근무인구           방문인구         총 유동인구  \\\n",
       "0  2018-01-01  317309.342098  22614.753707  198800.837073  538724.932927   \n",
       "1  2018-01-02  316696.629488  37324.649829  182846.761927  536868.041341   \n",
       "2  2018-01-03  315537.570146  37350.654659  183220.805780  536109.030707   \n",
       "3  2018-01-04  304965.323488  36979.035098  189812.450537  531756.809049   \n",
       "4  2018-01-05  312561.529732  35778.820512  184950.181756  533290.531878   \n",
       "\n",
       "          교통량      평균 속도   평균 소요 시간     평균 기온      일강수량     평균 풍속  confirmed  \\\n",
       "0  289.730488  41.819561  34.339293  3.105512  0.000000  2.661805          0   \n",
       "1  368.399268  40.727439  36.143439  4.321146  0.000000  2.128049          0   \n",
       "2  372.731073  40.526927  36.202805  3.508317  0.000000  2.984585          0   \n",
       "3  370.993512  40.265561  36.650073  2.739195  2.040683  2.270756          0   \n",
       "4  372.141561  40.186854  36.662341  2.639220  3.528463  3.083561          0   \n",
       "\n",
       "   death  released  tested  negative  daily  \n",
       "0      0         0       0         0      0  \n",
       "1      0         0       0         0      0  \n",
       "2      0         0       0         0      0  \n",
       "3      0         0       0         0      0  \n",
       "4      0         0       0         0      0  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 제주 데이터와, 코로나 데이터를 일자별로 맞춰 데이터를 합침.\n",
    "jeju_corona = pd.merge(jeju_mean,corona,how='outer',on='일자')\n",
    "jeju_corona.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "481ed300",
   "metadata": {},
   "outputs": [],
   "source": [
    "#https://tjansry354.tistory.com/12"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "355dcc5c",
   "metadata": {},
   "source": [
    "## 0으로 표시된곳은 코로나 이전. 코로나 이전이 확실히 많을 것을 볼 수 있음.\n",
    "## 확진자 발생 후 방문 인구가 확연히 줄어들다 시간에 따라 적응 후 제자리를 찾는게 보임"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "0615e1ce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(jeju_corona['confirmed'],jeju_corona['방문인구'],alpha=0.4)\n",
    "plt.xlabel('확진자 수')\n",
    "plt.ylabel('방문인구')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "693251b2",
   "metadata": {},
   "source": [
    "## 완치자와 방문인구의 상관관계를 봤을 때 초기에는 큰 영향이 없지만 점 점 늘어나는 것이 보임."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "80f30fd1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(jeju_corona['released'],jeju_corona['방문인구'],alpha=0.4)\n",
    "plt.xlabel('코로나 완치자')\n",
    "plt.ylabel('방문인구')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d4f9f4cf",
   "metadata": {},
   "source": [
    "# 이 유의미한 데이터를 이용하여 제주 방문인구를 예측해 보는 모델을 만들어 보려고함."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "cf2add99",
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
       "      <th>일자</th>\n",
       "      <th>거주인구</th>\n",
       "      <th>근무인구</th>\n",
       "      <th>방문인구</th>\n",
       "      <th>총 유동인구</th>\n",
       "      <th>교통량</th>\n",
       "      <th>평균 속도</th>\n",
       "      <th>평균 소요 시간</th>\n",
       "      <th>평균 기온</th>\n",
       "      <th>일강수량</th>\n",
       "      <th>평균 풍속</th>\n",
       "      <th>confirmed</th>\n",
       "      <th>death</th>\n",
       "      <th>released</th>\n",
       "      <th>tested</th>\n",
       "      <th>negative</th>\n",
       "      <th>daily</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2018-01-01</td>\n",
       "      <td>317309.342098</td>\n",
       "      <td>22614.753707</td>\n",
       "      <td>198800.837073</td>\n",
       "      <td>538724.932927</td>\n",
       "      <td>289.730488</td>\n",
       "      <td>41.819561</td>\n",
       "      <td>34.339293</td>\n",
       "      <td>3.105512</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.661805</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2018-01-02</td>\n",
       "      <td>316696.629488</td>\n",
       "      <td>37324.649829</td>\n",
       "      <td>182846.761927</td>\n",
       "      <td>536868.041341</td>\n",
       "      <td>368.399268</td>\n",
       "      <td>40.727439</td>\n",
       "      <td>36.143439</td>\n",
       "      <td>4.321146</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.128049</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2018-01-03</td>\n",
       "      <td>315537.570146</td>\n",
       "      <td>37350.654659</td>\n",
       "      <td>183220.805780</td>\n",
       "      <td>536109.030707</td>\n",
       "      <td>372.731073</td>\n",
       "      <td>40.526927</td>\n",
       "      <td>36.202805</td>\n",
       "      <td>3.508317</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.984585</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2018-01-04</td>\n",
       "      <td>304965.323488</td>\n",
       "      <td>36979.035098</td>\n",
       "      <td>189812.450537</td>\n",
       "      <td>531756.809049</td>\n",
       "      <td>370.993512</td>\n",
       "      <td>40.265561</td>\n",
       "      <td>36.650073</td>\n",
       "      <td>2.739195</td>\n",
       "      <td>2.040683</td>\n",
       "      <td>2.270756</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2018-01-05</td>\n",
       "      <td>312561.529732</td>\n",
       "      <td>35778.820512</td>\n",
       "      <td>184950.181756</td>\n",
       "      <td>533290.531878</td>\n",
       "      <td>372.141561</td>\n",
       "      <td>40.186854</td>\n",
       "      <td>36.662341</td>\n",
       "      <td>2.639220</td>\n",
       "      <td>3.528463</td>\n",
       "      <td>3.083561</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           일자           거주인구          근무인구           방문인구         총 유동인구  \\\n",
       "0  2018-01-01  317309.342098  22614.753707  198800.837073  538724.932927   \n",
       "1  2018-01-02  316696.629488  37324.649829  182846.761927  536868.041341   \n",
       "2  2018-01-03  315537.570146  37350.654659  183220.805780  536109.030707   \n",
       "3  2018-01-04  304965.323488  36979.035098  189812.450537  531756.809049   \n",
       "4  2018-01-05  312561.529732  35778.820512  184950.181756  533290.531878   \n",
       "\n",
       "          교통량      평균 속도   평균 소요 시간     평균 기온      일강수량     평균 풍속  confirmed  \\\n",
       "0  289.730488  41.819561  34.339293  3.105512  0.000000  2.661805          0   \n",
       "1  368.399268  40.727439  36.143439  4.321146  0.000000  2.128049          0   \n",
       "2  372.731073  40.526927  36.202805  3.508317  0.000000  2.984585          0   \n",
       "3  370.993512  40.265561  36.650073  2.739195  2.040683  2.270756          0   \n",
       "4  372.141561  40.186854  36.662341  2.639220  3.528463  3.083561          0   \n",
       "\n",
       "   death  released  tested  negative  daily  \n",
       "0      0         0       0         0      0  \n",
       "1      0         0       0         0      0  \n",
       "2      0         0       0         0      0  \n",
       "3      0         0       0         0      0  \n",
       "4      0         0       0         0      0  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "jeju_corona.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "b1354a8c",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# 데이터 전처리\n",
    "# 총 유동인구는 거주인구, 근무인구, 방문인구의 합 이므로 제거, 근무인구 또한 제거\n",
    "jeju_corona = jeju_corona.drop(['총 유동인구','근무인구',], axis=1)\n",
    "# 일자, 교통량, 평균 속도, 평균 소요 시간은 크게 영향을 받지 않으므로 제거\n",
    "jeju_corona = jeju_corona.drop(['일자','교통량', '평균 속도', '평균 소요 시간'], axis=1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "bd63b40f",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# Info를 보면 데이터의 수가 다른 것을 볼 수 있다. 이는 서로 다른 데이터를 합쳤을 때 나온 오류같다,\n",
    "# 오류들을 제거해보자.\n",
    "jeju_corona=jeju_corona.dropna(axis=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "5cb1d4eb",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 803 entries, 0 to 802\n",
      "Data columns (total 11 columns):\n",
      " #   Column     Non-Null Count  Dtype  \n",
      "---  ------     --------------  -----  \n",
      " 0   거주인구       803 non-null    float64\n",
      " 1   방문인구       803 non-null    float64\n",
      " 2   평균 기온      803 non-null    float64\n",
      " 3   일강수량       803 non-null    float64\n",
      " 4   평균 풍속      803 non-null    float64\n",
      " 5   confirmed  803 non-null    int64  \n",
      " 6   death      803 non-null    int64  \n",
      " 7   released   803 non-null    int64  \n",
      " 8   tested     803 non-null    int64  \n",
      " 9   negative   803 non-null    int64  \n",
      " 10  daily      803 non-null    int64  \n",
      "dtypes: float64(5), int64(6)\n",
      "memory usage: 75.3 KB\n"
     ]
    }
   ],
   "source": [
    "jeju_corona.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "510012a2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f3414dbc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 이 모델은 미지의 값을 예측해야하기 선형 회귀 모델로 코드를 작성하였습니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "de3c50b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 머신 러닝 수행\n",
    "# 학습용, 테스트용 데이터로 분리\n",
    "from sklearn.model_selection import train_test_split\n",
    "y_target = jeju_corona['방문인구']\n",
    "X_features = jeju_corona.drop('방문인구', axis = 1)\n",
    "X_train, X_test, y_train, y_test=train_test_split(X_features, y_target, test_size=0.2, random_state=11)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "68925959",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RandomForestRegressor 모델 : 0.5962794683615131\n",
      "LinearRegression 모델 : 0.5345448866208387\n"
     ]
    }
   ],
   "source": [
    "# 5주차 코드를 사용하여 두 가지 모델을 비교해보았습니다.\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.linear_model import LinearRegression\n",
    "\n",
    "# 2-1. 학습 객체 생성\n",
    "rf_reg = RandomForestRegressor()\n",
    "lr_reg = LinearRegression()\n",
    "# 2-2. 학습 데이터로 학습\n",
    "rf_reg.fit(X_train, y_train)\n",
    "lr_reg.fit(X_train, y_train)\n",
    "print('RandomForestRegressor 모델 :',rf_reg.score(X_test, y_test))\n",
    "print('LinearRegression 모델 :',lr_reg.score(X_test, y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d6ce573f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 하이퍼파라미터 튜닝 (GridSearchCV)\n",
    "from sklearn.model_selection import GridSearchCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "8c135f14",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GridSearchCV(cv=5, estimator=RandomForestRegressor(), n_jobs=-1,\n",
       "             param_grid={'max_features': [3, 5], 'n_estimators': [100, 200]},\n",
       "             scoring='neg_mean_squared_error')"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "param_grid = {\n",
    "    'n_estimators': [100, 200],\n",
    "    'max_features': [3, 5]\n",
    "}\n",
    "\n",
    "grid_rf = GridSearchCV(rf_reg, param_grid, cv = 5, \n",
    "                      scoring = 'neg_mean_squared_error', n_jobs = -1)\n",
    "grid_rf.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "2f8e2bd0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'max_features': 3, 'n_estimators': 200}"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grid_rf.best_params_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "68f7078c",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-152939848.5158996"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grid_rf.score(X_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "d1e28133",
   "metadata": {},
   "outputs": [],
   "source": [
    "from pandas import Series"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "700ffa15",
   "metadata": {},
   "outputs": [],
   "source": [
    "imp = Series(grid_rf.best_estimator_.feature_importances_, index = X_test.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "09153631",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZMAAAD4CAYAAAApWAtMAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAAcBUlEQVR4nO3deZRdVZ328e9DkYkhASRKBLVAggPgWCg0NAoubTQLacEBmwZBeKOggCItUWlaHMEBoyhDmEXlBZUGNI3ayqSAL1bU7qAIgqSBqCitJGhIgOR5/zi75HK5NZ5bt6pSz2etWnXuPnvvs8/JTf3WPvve85NtIiIi6thgrAcQERETX4JJRETUlmASERG1JZhERERtCSYREVHbhmM9gLGy5ZZburu7e6yHERExoSxZsuQB27ObyydtMOnu7qa3t3eshxERMaFI+p9W5bnNFRERtSWYREREbQkmERFRW4JJRETUNmkX4JcuX0H3gsVjPQwAlp0yb6yHEBFRS2YmERFR27gNJpIOlLRLP/teKemksn1aZ0cWERHNxvNtrmnA1H72XQ/8uGxv2pnhREREf8ZVMJF0CPAKYAqwDrhT0luBV5fXt9v+NDAHeCvw2Ya2+9m+smw/F9jA9i87fAoREZPSuLnNJWkrYBfbhwNvA55Rdu1h++22jwB2LmVTgOlNXRwkSWX7KODBFseYL6lXUu/aVSvafg4REZPVuAkmwK7A1QCu0j9eWcpPlPQmSZ8EWq6hFD8EdpfUBTzF9m+bK9heZLvHdk/XRrPaPPyIiMlrXN3matI3yzgP+AywGNhygPqXAh8CNga+O7pDi4iIRuNpZnIzMA9A0gbAflTB7j9t3wSsAbbtr7HtPwCbAwcAl4/6aCMi4m/GzczE9v2SbpZ0EdXs4jZgFdAj6UtUge8Pkv4JuA54uDR9qKGb7wKvtf2Xzo08IiLGTTABsP0V4CtNxT/pp/pppc1xDWXTWrSPiIhRNq6CSR2S3g/sCBw6lPo7bz2L3jzGJCKiLdabYGL7U2M9hoiIyWo8LcBHRMQElWASERG1JZhERERtCSYREVFbgklERNSWYBIREbUlmERERG0JJhERUVuCSURE1LbefAN+uJYuX0H3gsVjPYwnWZZHvETEBJSZSURE1DYugomkAyUNlEWxVZtdJb2xbL9FUs/ojC4iIgYzLoIJ1aPjp46gzbSyPb1hOyIiOmzM1kwkHQK8ApgCrAPulLQPsD9VcLjE9tWl7seApwIbARfb/i5wFLClpF+XLg+UdDgwA/ik7f/u6AlFRExiYxJMJG0F7GL7cEkCvl/Gsrvt+aXOBZJ+AGwFPGT7xFL3AqqMimcA29i+RdLzgDttf17SxsCpwLtbHHc+MB+ga+bs0T/RiIhJYqxmJrsCVwPYtqQrgceAPSSdWepsDmxl+x5Jl5VZx07AFv302Vv6+6uklre8bC8CFgFMmzPXbTubiIhJbrx8NFjl95W2FwJI6rK9VtJeVLe+zgYuBM4akxFGRES/xmoB/mZgHoCkDYD9SvneKoCvlX09wBm2b6Walcxq6EdERMSYG5OZie37Jd0s6SJgY+A24BHgXOCrpdrFttdJ+ibwMUkPlPKNJO0M/BL4kKQ7gdXAmoZDPNSRE4mICABkT86lg56eHvf29o71MCIiJhRJS2w/6Xt94+V7JhERMYElmERERG0JJhERUVuCSURE1JZgEhERtSWYREREbQkmERFRW4JJRETUlmASERG1JZhERERt4+WpwR23dPkKuhcsHuthTErLTpk31kOIiDbLzCQiImpLMImIiNo6EkwkndaJ4zQc7wRJT+3kMSMiJrNOzUw27dBx+kwHpnT4mBERk1btBXhJTwdOBx4GPgL8C7AWWGb7lKa6WwAfLy8fAhaUBFh7A4dSJbl60Pb7JT2FKkXvn4FNgCNtr5C0D1Ua3+nAJbavLn0fD+wAzCg/ERHRIe2YmUwB/mz7n6kCwpG23wk8KumlTXXfBZxg+0jg/wFvKOUH2D7E9nxgSgk6ewFfLmXnArtJmgbsbnu+7UOAN0uaKuklwNRS9whgx1YDlTRfUq+k3rWrVrTh1CMiAtr30eC7y+9XAZtXKdzZBPgNsKSh3m7A08v+qcBPS/n7Je0LvAx4BfAZ4BrgXEk7AJfavk/Si4A9JJ1Z2m0ObAXsCVwBYHuNpKtbDdL2ImARwLQ5cydnismIiFHQ7u+Z/KrMOlCJGE0e6Ntf6nRJ2hD4CtWtsk8DjwHY/hOwv6Qe4JOSvkSV5/1K2wv72tte2+JQrY4dERGjpN0L8FMlbVm2TwRe2LR/paTnAkg6GNiXanZxh+1rbK8Eti/73ybpJbZ7qYLMHsBtwN4qgK9J2gC4nmodBUnTgde2+bwiImIA7ZiZPEq1+A5wEnCGpL8Cv7b981L+UPn9EeBzkh4GVgLHlwX4KZLOKHVWAwdTrZMslPQQsBnwfturJZ0LfLXUvdj2OuBnkvaWdD4wE7i5jCsiIjpA9uRcOujp6XFvb+9YDyMiYkKRtMR2T3N5vgEfERG1JZhERERtCSYREVFbgklERNSWYBIREbUlmERERG0JJhERUVuCSURE1JZgEhERtSWYREREbe1+avCEsXT5CroXLB7rYUQNy06ZN9ZDiIgiM5OIiKgtwSQiImqrHUwkbSnpcknXSrpM0qxSfrSkrcv258r+ayXdLGmPUv6pAfo9QNLf9bPvuIb+fixpt8H6i4iI0dOONZMTgBNt/7LkYj+WKm/J1L7+bb+3r7KkF1MlzfoRMGOAfl8OPAjc1GLf56nS9Ap4KbB1Kd9K0gnAmSXRVkREdEA7bnNtavuXALZ/CmwxSP1dgJ+V7a3K7OJpjRUkHQ7cCvxV0lta9PGvVJkXe4BVwFWlfIXtU/sLJJLmS+qV1Lt21YqhnFtERAxBO2Ymv5Z0KPANqgyJv2hVSdLGwD8C023/Vyn+ve03NdQ5BNgJWGz7+lL2eklfAK6zfXmpOgu4jCpf/FOBV0raghKcgH+2vbx5DLYXAYsAps2ZOzmzgkVEjIJ2BJMvARcAHwWuoUq1+0LgB8B9AJLeC6wFvmX77oa2axo7sv3l5s5tX8XjM48+nwcOB0x1K+wu4Dpgl8bgFBERndGOYDIV+Hb5AXh++f16YD7VrafPlUXyBZK6qWYUtwNn93UiaVOqdZC+W2+zgUeAvvtRq4HXubJM0o+BtwPbUgWlpcBn23A+ERExTO0IJo8AbwQ2ayrfhCpoIGlH4G3AJ4F7qQLGc4BTJb3V9sO2HwJe1ddY0gFUt8FubD6gpO2BdwCfAJaX83gusBB4cxvOKSIihqEdwWQH4HrbCweoY6pPXm0IdFEFkw1L+UjWLjZo+Onrf4PSd0REdJjseuvQkqYDX6X1p7g+aPvmUu9lwKFAN9WM5VfA2bbv6qffFwMPNq2xNO5/GXBY6e8RqttcZ7ZaeG+lp6fHvb29Q6kaERGFpCW2e5rLa89MbK8GDhhCvVuAW4bR788G2T+s/iIiYvTkcSoREVFbgklERNSWYBIREbUlmERERG0JJhERUVuCSURE1JZgEhERtSWYREREbQkmERFRWzuezTUhLV2+gu4Fi8d6GDHOLDtl3lgPIWJCyswkIiJqG9fBRNKBknrK9r9JeuXYjigiIloZ77e5ppUfgFOBNZJmNuZ4b34dERGdVzuYSHo68EFgY6rUvLfaXijpOODZwEzgw7bvkjQN+DRVgFgH2PZRkrqoUvFuSJXf/VPAHVQJtVZK+j2wC1V63oMknWL795JmAx8G3iVpH2B/YDpwie2r655bREQMTTtmJlOAHYFX235M0gUlF8nvbJ8maRPgNKoUvkcC37B9g6QdeDy3++7AD21fKmkW8FHbx0i6CLizBKI9qFIEXwnsR5Xy9/XAFSVI7W57PkAZww9sP9I4UEnzyzjomjm7DaceERHQvttc37f9WNl+DHgFsIukPUvZrPL7+X0ZGW3fIWlp2b5B0vMlHUUVmKYOcKwbqHK/nw3sCRwO7ATsIenMUmdzYCvgnsaGthcBiwCmzZlbLytYRET8zWitmQj4tO2fA5TbWK247D8Y2A64BDiT8ge/ZQN7raQ/S3omsKLMhgRc2ReoJHXZXtuuk4mIiIGN1qe5bgTeDCBpc+CsUv4rSbuX8u2BnUv5rsCnbN9Btc7SSC36v4Iq6FxRXt8G7K0C+Jqkcf1JtYiI9Uk7ZiaPAA83vH7I9i2S9pF0HtXC/Ill3xnAZyQdQRXI/quUXwScK+kBYA3w7LKw/1PgVEnHlvI1pf71wCfLb2yvlnQuVS56gIttr2vDuUVExBDI7tzSgaTXATfZflDSDOA82//UsQE0mDZnrue8beFYHDrGsXwDPmJgkpbY7mku7/T3TO4GzpL0ILApcEqHj/83O289i9784YiIaIuOBhPbtwEHdvKYEREx+rJIHRERtSWYREREbQkmERFRW4JJRETUlmASERG1JZhERERtCSYREVFbgklERNSWYBIREbWN97S9o2bp8hV0L1g81sOIcSzP6YoYusxMIiKitgSTiIiobdi3uSQtAuY2FN1l+whJC4BzbP9vqTcPOL5FF5sB82z/tkXfU4HF/YzrOtsnt2jTBXzZ9kHDPZeIiGiPkayZvAPYy/Y1kvYCNpZ0LdANXNBXyfZiqsDwBJIOogpGTwomth8BXi3pINtfLfW7gP1tf71FX1sAHwcekPQBYKHth5vrRUTE6Br2bS5X2bT2Ky9fB3zH9l7AhUPsYlNaBJImuzZs7wTMatwp6QUlgJ0JnAf8K7AU+Lqk6yTNbNWppPmSeiX1rl21YojDjYiIwYz001x96Rm7gMMkvYvqD/5ZAJI2Aq4q+5u9EviepNc2p9Ytt7n+A+gqwaJx3zNtnwRg+7+BvRr2nW77aODbAw7aXgQsgirT4tBONSIiBjOsYFJS7R4JrJR0PHAP8CDVH/Z3A2tL1XXAxWX74IbtlwM3Abf2k6P9RcDpDa//Hvhhw/GfZvt+SccB+zbUm90UfL5g+9+Hc24RETFywwomZT3iNEkvAI4Ang08BuxCtfj+QKm3WtKXbVvSLrYvApC0GrjP9o399H+LpGcC/wfYEXgD8HTgOuAC24+WeqcBpw37bCMiYlSM5NNczwCOAT4B3Ee17rIt8DFJh9leVaruL+kx4IaG5vcCfxyg7w2AbwE/Am4BbgQ2Bv4BeA7wvoa63wI2ae4C+LHtBcM9r4iIGLmRrJl0UQWQvsV7l23xxAX9LmC17Sv7CmzfNEjfApYAXwD+B3iEasH+RcDejRVt79vcGEDSWUM5iZ23nkVvvuEcEdEWww4mtpdJOh14D7Ad1TrJ7cCJtv/SUPWHwAVlbaXZB2z/uEXfayV9mOo2105Us5IHqG5zfWyIQ7xmiPUiIqJNVH3Sd/Lp6elxb2/vWA8jImJCkbTEdk9zeR6nEhERtSWYREREbQkmERFRW4JJRETUlmASERG1JZhERERtCSYREVFbgklERNQ20kfQT3hLl6+ge8GTcndFjBvL8rifmEAyM4mIiNoSTCIioraOBRNJV0h6s6QZkv5jlI+VXCcRER3UyTWTP9q+DEDSAaN8rE1Huf+IiGgwpGAi6WCq3O1TgcXApcBHgKdSPSb+VNtLJR0IzAW6gWnAebavlfRuYA9Jb7T9DarHyb9P0gnAVsBdwDeBz1DlMJkGXA7Mo5o9fdP2VZKmUyXlmkGVR+V9th+W9Czgo8AqBki+FRERo2PQYCJpK2BX24eX1/8XWA3cYftfyx/4C4EDqYLANNuHl6yJ5wDX2v6ipBeWQAIws/yeThUoflQCwhrbb5c0kypo7VnqXQJcRZUqeKHteyS9FDgK+CxwEnC07RWSDqEKUK3OZT4wH6Br5uyhXqOIiBjEUGYmu1L9Ye/zVqr86yfC3/K93ytpVtl/dSlfJ2ndEPq/u2H7rtJ2paRfuSRbkfRw2f9yYEdJUGVl7JuFrLW9omxfAfx9qwPZXgQsApg2Z+7kTOQSETEKhhJMNqC6pdTnmTx54V5tG9HA1tk+8m8Hlbpa1OnUWCIiohjKp7l+QrV20efTwA+ANwFImgFs0zAzGE2/kPSactw9gXeX8g0kbVa239CBcURERINBZya275V0q6TzSv3FwLeAk0vZDKrFb6jWUtY0NH+oYbsx2Kwsvx8GHi3bj5b2ff7Sov4XgdMlvYlqBnJ0Kf8I8MVyW21Z07EiImKUJQd8REQMWXLAR0TEqEkwiYiI2hJMIiKitgSTiIioLcEkIiJqSzCJiIjaEkwiIqK2BJOIiKgtwSQiImpLMImIiNo6mWlxXFm6fAXdCxYPXjFiAll2yrzBK0WMgsxMIiKito4GE0mfHe02kk6Q9NThHiciIkau0zOTmYNXqd1mOjBlBMeJiIgR6tiaiaQ3A3tIOha4Hdif6g//JbavlrQ9VeKtP5RxvaPU2UPSsbY/L2mf5nal7+OBHahyq8zo1DlFRESlY8HE9mWSXg2cBZxoez6ApAsk/QD4R+Ak20slHQI8t69NCSTTgN1btNsJmGp7fqnz8/7GIGk+MB+ga+bs0TvZiIhJZiw+zfU8qtnGmeX15sBWwL8Dn5X0HeDrtv93iO32BK4AsL1G0tX9Hdj2ImARwLQ5cydnVrCIiFEwFsFEwJW2FwJI6rK9tmzvD+wBnCvpONt3D9ZOUqv+IyKigzq9AC/gNmBvFcDXJG0g6UTgKbZvAC4AXtrQhv7aAddTraMgaTrw2g6eT0RE0PmZyRrgKOBc4Kul7GLb6yRdCiyUtBLYtNQDWFNmKadJelI74GeS9pZ0PtUnv24GHu3UCUVEBMienEsH0+bM9Zy3LRzrYUS0Vb4BH6NN0hLbPc3lk/ZxKjtvPYve/MeLiGiLPE4lIiJqSzCJiIjaEkwiIqK2BJOIiKgtwSQiImpLMImIiNoSTCIiorYEk4iIqC3BJCIiakswiYiI2ibt41SWLl9B94LFYz2MiBiGPHts/MrMJCIiakswiYiI2oZ9m0vSImBuQ9Fdto+QtAA4py/drqR5wPEtutgMmGf7ty36fg3wgfLSVDlLLpC0GfBO26c01X0PMAXoKsX3Agts/2645xURESM3kjWTdwB72b5G0l7AxpKuBbqpMiQCYHsx8KRFCUkHUQWjJwUT298DvlfqbQCcUfrsAqY19DEFOBI4wPbDDeXPAU4q+yIiokOGfZvLVTat/crL1wHfsb0XcOEQu9iUFoGkxXHWAav72fcocCuwUdOumcBP+utT0nxJvZJ6165aMcThRkTEYEb6aa6+9IxdwGGS3gXMAs4CkLQRcBWP335q9Erge5JeWwLGQKYNsO8jVDnhZwJvpwpmt9k+v99B24uARVBlWhzk2BERMUTDCiaSZlDdQlop6XjgHuBBYC/g3cDaUnUdcHHZPrhh++XATcCtgwUSSdsCt/ez72Rgz4ai7YF3ln0AJ9u+buhnFhERdQwrmJT1idMkvQA4Ang28BiwC9Xi+wOl3mpJX7ZtSbvYvghA0mrgPts3DuFwxwIn9zOOf5P0PNu3DWf8ERExOkbyaa5nAMcAnwDuo1p32Rb4mKTDbK8qVfeX9BhwQ0Pze4E/DtD3NGA34EDgAtt/HmAox5CF9oiIcWEkayZdVAGkb/HeZVs8cUG/C1ht+8q+Ats3DdL3rsCWwPts/3WQujOGM+iIiBg9qj6cNcxG0ouBw4HtqNZJbgcW2b6joc4cqo/1tlpE/4DtHw/zmDNtr2x4/QmqWUyz621/eLD+enp63NvbO5whRERMepKW2O5pLh/Rp7ls/4xqwX2gOr8D9hlJ//30t7Lp9Qfb1XdERNSTx6lERERtCSYREVFbgklERNSWYBIREbUlmERERG0JJhERUVuCSURE1JZgEhERtY30EfQT3tLlK+he8KTcXRER67Vlp8wblX4zM4mIiNoSTCIiorYEk4iIqK32momk04AXl5d/BY6x/RtJRwOX215e6s0Dju+nmyc8RVjSMcDewNW2zy5lzf3tDnysRV8rgHfa/n3dc4uIiKGpHUxsH9e3LWlXqhS+vwGmNvZvezGwuNQ7Avi97W839yfpUKoZ0yHA0ZL2t315i/5uLMdqbr8vVUrfy+qeW0REDE27b3M9zON54FuStD3wUmA/SVu1qLKb7YXlkfOf5Im53ofiwf7GIGm+pF5JvWtXrRhmtxER0Z92fzR4G+BZkq4FngF8o29HmY08H/g98B6qpFnHStoU6LXdrpnEZsD9rXbYXgQsApg2Z+7ws4JFRERL7Q4mLwbOsH2ypPc17rB9blPdNcBHW/Rxs6T3AOcDR/PEHPIASBLwfapbX832AH4qaa/mhFoRETE62hZMyi2rmbb/2GLfpsAVPH5bbTbwCNViOcBq4HWucghfBJwAXEy1AH95qbOqtMG2JV3I48FkLrA5cAtwIbCO6sMAERHRAe34NNfTgNcAfwe8r1Ud2w8Br2pocwDVAvyNLapvAzxie7+mPs5sen1xQ3+7A9vYvnSk5xERESPXjpnJ64GljX/caxIws0199WvnrWfRO0qPFYiImGza8dHgc/rZtQj4Sz/7fkP1qatWfgtsUxbxm33c9vdblK+gWtCPiIgxMGoPeiy3tvrb97MB9j0GHDHMY906nPoREdFeeZxKRETUlmASERG1JZhERERtqr7aMflIegi4fazHMc5tCTww1oMY53KNBpdrNLiJdI2eZXt2c+GkzbQI3G67Z6wHMZ5J6s01Gliu0eByjQa3Plyj3OaKiIjaEkwiIqK2yRxMFo31ACaAXKPB5RoNLtdocBP+Gk3aBfiIiGifyTwziYiINkkwiYiI2tbLYCJpH0mXSLpU0jNb7H+xpMvKz4sayg+VdLGkr0ia1dFBd1iNa/QDSeeUnwM7OugOG+walTrbSPqXprJJ8z6CWtcp76XH9x9c3jMXS3pLQ/nEeS/ZXq9+qB5hf1HZ3hw4vUWd84Ep5ef8UjaTKkskwPbAh8f6XMbhNZoKLBzr8Y+ja7Qj8G3gQw1lk+Z9VPM65b30+P7pff/HyuuLyv+7CfVeWh9nJi8Fbgaw/WdgRknzC4CkpwL3237U9qPA/ZJmUyX4uqq0u5Mqh/36aqTXaDtgO0nnSvq8pE3GYvAdMuA1KuW/AN7V1G4yvY9g5Ncp76XHbQT8Z8PrPwEzmGDvpfUxmHQDdzW8/gOwRcPrZ1LlU+lzdylrbrd2dIY3LnQzsms0Hfim7SOAs4FTRneYY6qbga/RUNutz+8jGPl1ynupsP0n25cASHoWVfrzlS3ajev30mR+nEoMk+2fAz8v27+UNGNMBxQTVt5LTyZpX+AVwNFjPZaRWB9nJsuoptB9ZlNNG/vcA2zb8Lq7lDW3Wx+vTZ9ljOwaNVufv6S0jIGv0VDbrc/vIxj5dWo2qd9Lkg4Dnmb7eNur+mk3rt9L43pwI7QE2BVA0mbAw7YtaQ6A7T8AT5O0oaQpVP+AfwS+B+xb2m0H3DcWg++QEV0jSe+V9LzSbjbVrYr11YDXaACT6X0EI7xOeS89fo0kzQR2sH1uU7sJ9V5a725zlX+kSyV9BegCTpC0EdVC1i6l2peAi8v2qaXdSkm9ki4o7SbkVHMoRnqNqD5lcpqk1cCmwIc6OOyOGuI1AngEWNXQbtK8j2Dk14m8lxqv0UuA3SSd09DsRNv3T6T3Uh6nEhERta2Pt7kiIqLDEkwiIqK2BJOIiKgtwSQiImpLMImIiNoSTCIiorYEk4iIqO3/A/TYFzI+q6NAAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "imp.sort_values(ascending = False).plot(kind = 'barh')\n",
    "# 거주인구, 평균 기온, 검사자 수, 미감염자, 총 확진자 수가 가장 영향을 많이 받는것으로 보여짐"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "d9935d7d",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# 예측한 모델을 시각화 해보자\n",
    "# 하이퍼파라미터 튜닝 모델을 가지고 시각화 해보자\n",
    "model = grid_rf.fit(X_train, y_train)\n",
    "x_new=X_test\n",
    "# 예측된 방문객 수이다.\n",
    "y_new=model.predict(x_new)\n",
    "# 실제 방문객 수와 예측된 방문객 수를 보자.\n",
    "y_compare={'실제 방문객 수':y_test, '예측 방문객 수':y_new}\n",
    "y_compare=pd.DataFrame(y_compare)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "50122f07",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAFgMAAAJGCAYAAADYYTHBAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAACMYElEQVR4nOzdf4zldX0v/ud7dhYHCxks2JTLfmUAEfUPAhFBQUWF8MPVkGKaFiH88OoWUpYLxoUxizJiwRFKEdSwYhGCNKBtNdA7RWsLvSVISaGkubR6g/SODWkCsnaHX7sXZvf9/YNh3GVn55zdnc85Z848HonxnPfndT7zPCzMnh+fz/NTaq0BAAAAAAAAAAAAAAAAAAAAAAAAAAAAmjPQ7QAAAAAAAAAAAAAAAAAAAAAAAAAAAADQ75QBAwAAAAAAAAAAAAAAAAAAAAAAAAAAQMOUAQMAAAAAAAAAAAAAAAAAAAAAAAAAAEDDlAEDAAAAAAAAAAAAAAAAAAAAAAAAAABAw5QBAwAAAAAAAAAAAAAAAAAAAAAAAAAAQMOUAQMAAAAAAAAAAAAAAAAAAAAAAAAAAEDDBrsdYCHst99+dWRkpNsxAAAAAAAAAAAAAAAAAAAAAAAAAAAAWOIeffTRZ2utb379el+UAY+MjOSRRx7pdgwAAAAAAAAAAAAAAAAAAAAAAAAAAACWuFLKL+ZaH+h0EAAAAAAAAAAAAAAAAAAAAAAAAAAAAFhqlAEDAAAAAAAAAAAAAAAAAAAAAAAAAABAw5QBAwAAAAAAAAAAAAAAAAAAAAAAAAAAQMMGux0AAAAAAAAAAAAAAAAAAAAAAAAAAACAHXvllVfy1FNPZdOmTd2OwlaGhoayYsWKLF++vK15ZcAAAAAAAAAAAAAAAAAAAAAAAAAAAAA97Kmnnsree++dkZGRlFK6HYcktdasX78+Tz31VA466KC2HjPQcCYAAAAAAAAAAAAAAAAAAAAAAAAAAAB2w6ZNm7LvvvsqAu4hpZTsu+++2bRpU9uPUQYMAAAAAAAAAAAAAAAAAAAAAAAAAADQ4xQB956d/TNRBgwAAAAAAAAAAAAAAAAAAAAAAAAAAAANG+x2AAAAAAAAAAAAAAAAAAAAAAAAAAAAANo3MjqxoPubHF/Z9uyaNWty7bXXzt7/2te+ltNPPz0HHHBAkmTdunX57ne/myQppeT73/9+rrrqqlx88cW55557csEFF2y3z4ceeijPPvtsPvaxjyVJrrjiinzxi1/M3Xffnf322y/HHXfc7Oxpp52W5557bpvHb9myJSeddFLWrl2bJPnRj36U8fHxJMkb3/jGTExM5NJLL80111yTtWvX5qqrrmrreY6Pj2fZsmVt/7NpRRkwAAAAAAAAAAAAAAAAAAAAAAAAAAAALa1fvz7/9E//lBdffDG/8Ru/kSR5+eWXMz09PTtz/vnn57zzzsvll18+Wxr8wgsvZHp6Oi+//PKc+3355Zfz7W9/Oz/5yU+SJI899liSZHp6ept9J8n++++fu+++e7t9nH/++bO3Tz755Jx88slJktWrVydJNm7cmCR56aWXWj7PLVu25OGHH84DDzyQD37wgy3n26UMGAAAAAAAAAAAAAAAAAAAAAAAAAAAgJa+/OUvZ3x8PJdccknWrFmTQw89dM65LVu2ZMuWLTu177POOisf//jHkyRr1qyZXb/44otz8cUX55xzzknyaiHxV77ylW0eOz09nf3333/O/dZakyTPPvtsrrvuujzzzDPz5ti4cWPGxsZyww035JZbbsnw8HCOPPLInXouO6IMGAAAAAAAAAAAAAAAAAAAAAAAAAAAgHmNj4/nlFNOyXve854cccQR+fSnP51vfetbc86uX78+69evz80335w777wzb3/72+fd9/DwcO67776MjIyk1prnn39+dttXv/rVHH/88bP377rrrrzwwgvbPH5gYCB77733dvv9wQ9+kAMPPDBJss8+++Tcc8/N5OTkDnOMjY1leno6q1atyiGHHJLrr78+69aty6233ppPfepTOfzww+d9Hq0oAwYAAAAAAAAAAAAAAAAAAAAAAAAAAGBeH/3oR7N58+b8y7/8S5LkwgsvzE9/+tOccMIJWbFixTazjz/+eP7zP/8zq1atyqpVq3LBBRfMu+8jjjgimzdvzoYNG5IkV1xxRZJk2bJlWbZs2ezcF77whTzwwAOz9zdu3Jg999xz9v7atWtz4okn5rbbbst3vvOdnHDCCbnsssuSJOedd1723XffnH322TvMMTY2ts395cuXZ/Xq1fNm3xnKgAEAAAAAAAAAAAAAAAAAAAAAAAAAAJjXihUrMjExsd36Pffck5tvvjnDw8Oza3/3d3+X3/md38ljjz2WI488sq39H3zwwVm3bl0effTRvPjii1mxYkXOOuusvO9975udufLKK7d5zCWXXJLrr79+u32dc845Offcc7dZO/roo5Mk7373u+f8+Q8++GAuv/zy2fs///nP89a3vnX2/jHHHJPx8fG2nsuOKAMGAAAAAAAAAAAAAAAAAAAAAAAAAABgXnvssUf+/M//PFNTU9usv/DCCxkc/HXN7YMPPpiDDz44n/zkJ/PpT386N998c1v7/8xnPpNVq1bloosuyh577JGnn346N954Y5YvX55jjz12du5LX/pSPv/5zydJDjvssDn3VUrJqaeemk2bNm237fDDD88NN9yw3fpxxx2X+++/f/b+joqGd4cyYAAAAAAAAAAAAAAAAAAAAAAAAAAAgEVkcnxlx3/mz372s5x44om58MIL5517/PHHc/7556eUktHR0Tz++OMppbTc/+bNm7N58+Ykr5b51lpTa8309PQ2c08++eTs7fPPP3+H+7v33nvnXL/kkktaZmlKqbV27YcvlKOOOqo+8sgj3Y4BAAAAAAAAAAAAAAAAAAAAAAAAAACw4H7605/mHe94R1czbNy4MZ/4xCeyYcOG7bZdffXVee9737vDxz733HPZe++98+KLL2avvfaac2b9+vW56aab8s///M956aWXcsABB+TMM8/Mhz/84W3mRkdH8/DDD2/3+OOPPz5jY2Mtn8eGDRuyzz77tJz7/ve/n9NPP73l3Fx/NqWUR2utR71+VhkwAAAAAAAAAAAAAAAAAAAAAAAAAABAD+uFMmDmtjNlwAMdSwUAAAAAAAAAAAAAAAAAAAAAAAAAAABLlDJgAAAAAAAAAAAAAAAAAAAAAAAAAAAAaJgyYAAAAAAAAAAAAAAAAAAAAAAAAAAAAGjYYDtDpZQ1Sd6Z5A1JvpXkfyV5JMmjMyPfq7X+uJSyPMlNM/v911rrtTOPPzDJNUm2JLm11vo3M+unJDknr5YSr6m1/sfM+qUzP++VJBfUWqcX4LkCAAAAAAAAAAAAAAAAAAAAAAAAAABAV7QsAy6lHJTkTbXW80opJcmfJflFkj+rtV73uvGzk9xRa/37UsoVpZRDa61PJPlskj+otW4opdxeSvnxzPwZtdYzSilvSnJlktWllEOTDNVazy2lfCivlgXfsjBPFwAAAAAAAAAAAAAAAAAAAAAAAAAAADqvZRlwkj2T/DhJaq21lLIpyduSHFVK+VaSp5OM1Vqnkxxba32tuPd7SU4rpVyXZM9a64aZ9YeSvGur26m1/lcpZc+ZsuHTZh6bWuv9pZQzowwYAAAAAAAAAAAAAAAAAAAAAAAAAADgVWPDC7y/qZYjW7ZsyZo1a7Jhw4Z8/etfz5577pnR0dGsXr0699xzTy644IJt5teuXZuf/OQnSZKVK1fms5/97A73/dBDD+XZZ5/Nxz72sSTJFVdckS9+8Yu5++67s99+++W4446bnT3ttNPy3HPPbZftpJNOytq1a5MkP/rRjzI+Pp4keeMb35iJiYlceumlueaaa7J27dpcddVVLZ/vmjVrMj4+nmXLlrWcbVfLMuBa678l+bckKaUcmeRXSUqS22qtPyqlfDjJaJI/SrJ5q4c+meTAJPvm1cLg16+XmduveSbJbyYZSfLvW61v2alnBAAAAAAAAAAAAAAAAAAAAAAAAAA9YmR0ouXM5PjKDiQBgN3zl3/5lznssMNywAEHZN26dbnkkkvy4osvZnp6Oi+//PLs3L333ptrrrlmm8dOTExkYmIiV199dd773vdut++XX3453/72t2fLgx977LEkyfT0dKanp7eZ3X///XP33Xdvt4/zzz9/9vbJJ5+ck08+OUmyevXqJMnGjRuTJC+99FLL57ply5Y8/PDDeeCBB/LBD36w5Xy7WpYBv6aU8t+T/Lckl9VaZ0t/a633lVLOXLBE26s7yLMqyaokectb3tLgjwcAAAAAAAAAAAAAAAAAAAAAAAAAAFjaHnjggVx33XVZvnx5PvrRj+aee+7JIYccst3cqaeemlNOOSWPP/54brzxxrzhDW/IRRddlLe97W3z7v+ss87Kxz/+8STJmjVrZtcvvvjiXHzxxTnnnHOSJOvXr89XvvKVbR47PT2d/ffff8791vpqve2zzz6b6667Ls8888y8OTZu3JixsbHccMMNueWWWzI8PJwjjzxy3se0q60y4FLK55L871rrLTsYea2wd2CrtYOT/CLJ+iS/9br1R2Zuv2ur9Tcn+VWSySQHJfk/c+zz1z+w1puT3JwkRx111JyFwQAAAAAAAAAAAAAAAAAAAAAAAAAAAOy+LVu2ZPny5UmSiy66KDfccENWr1693dydd96ZJ554Iu985zvzta99LdPT07nnnnty55135phjjskpp5yy3WOGh4dz3333ZWRkJLXWPP/887PbvvrVr+b444+fvX/XXXflhRde2ObxAwMD2Xvvvbfb7w9+8IMceOCBSZJ99tkn5557biYnJ3f4HMfGxjI9PZ1Vq1blkEMOyfXXX59169bl1ltvzac+9akcfvjh8/9DaqFlGXAp5ZAk/6/W+j+3Wvtykmtrrb8qpbw9yWvP/qFSygdqrf+Q5HeT3FVrraWUTaWU4VrrVJL3JPnmzPwfJvlmKWWfJBtnZu9O8ntJ/qiUcnySf9ytZwgAAAAAAAAAAAAAAAAAAAAAAAAAAMBu2bJly5y3t/bCCy/klltuyebNm3P//ffnG9/4xjbbH3rooZx00kkZGBjYZv2II47I5s2bs2HDhiTJFVdckSRZtmxZli1bNjv3hS98IQ888MDs/Y0bN2bPPfecvb927dqceOKJue222/Kd73wnJ5xwQi677LIkyXnnnZd99903Z5999g6f49jY2Db3ly9fPmfh8a5qWQac5P1JPlxKecfM/c1Jrk9yYynlhSRDST4zs+32JN8opZyd5Ge11idm1v84ybpSyuYkt9daa5KUUr5bSrkjybIklyVJrfWJUsrLpZQ/nflZF+72swQAAAAAAAAAAAAAAAAAAAAAAAAAAGCXDQwMZPPmzVm2bFm+/vWv5/HHH88hhxyyzcxee+2Vv/3bv92l/R988MFZt25dHn300bz44otZsWJFzjrrrLzvfe+bnbnyyiu3ecwll1yS66+/frt9nXPOOTn33HO3WTv66KOTJO9+97vn/PkPPvhgLr/88tn7P//5z/PWt7519v4xxxyT8fHxnX5eW2tZBlxrvS3JbXNsOmuO2VeSrJpj/RdJzphj/YdJfjjH+jWtcgEAAAAAAAAAAAAAAAAAAAAAAAAAANAZRx99dP7qr/4qBxxwQK6++up87nOfy+rVq7eb++u//utce+21262/9NJLuf3223PYYYfNuf/PfOYzWbVqVS666KLsscceefrpp3PjjTdm+fLlOfbYY2fnvvSlL+Xzn/98kuxwX6WUnHrqqdm0adN22w4//PDccMMN260fd9xxuf/++2fv76hoeHe0LAMGAAAAAAAAAAAAAAAAAAAAAAAAAACgh4xNdfxH/v7v/37OOeecPP/887njjjuSvFq6+3of+chH8pGPfGS79b/4i7/IU089tcMC382bN2fz5s2z+621ptaa6enpbeaefPLJ2dvnn3/+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AAAAAF5vZHSi5czkUAeCACyQgW4HAAAAAAAAAAAAAAAAAAAAAAAAAAAAgH6nDBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAapgwYAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqYMGAAAAAAAAAAAAAAAAAAAAAAAAAAAABqmDBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAapgwYAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqYMGAAAAAAAAAAAAAAAAAAAAAAAAAAAABqmDBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAapgwYAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqYMGAAAAAAAAAAAAAAAAAAAAAAAAAAAABqmDBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAapgwYAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqYMGAAAAAAAAAAAAAAAAAAAAAAAAAAAABqmDBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAapgwYAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqYMGAAAAAAAAAAAAAAAAAAAAAAAAAAAABqmDBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAapgwYAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqYMGAAAAAAAAAAAAAAAAAAAAAAAAAAAABqmDBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAapgwYAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqYMGAAAAAAAAAAAAAAAAAAAAAAAAAAAABqmDBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAapgwYAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqYMGAAAAAAAAAAAAAAAAAAAAAAAAAAAABqmDBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAapgwYAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqYMGAAAAAAAAAAAAAAAAAAAAAAAAAAAABqmDBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAapgwYAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqYMGAAAAAAAAAAAAAAAAAAAAAAAAAAAABqmDBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAapgwYAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqYMGAAAAAAAAAAAAAAAAAAAAAAAAAAAABqmDBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAapgwYAAAA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AAAAAAAAAA7MZsAAAAAAAAAAAAAAAAAAAAAAAAAAAABwYDYDBgAAAAAAAAAAAAAAAAAAAAAAAAAAgAOzGTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcmM2AAQAAAAAAAAAAAAAAAAAAAAAAAAAA4MBsBgwAAAAAAAAAAAAAAAAAAAAAAAAAAAAHZjNgAAAAAAAAAAAAAAAAAAAAAAAAAAAAODCbAQMAAAAAAAAAAAAAAAAAAAAAAAAAAMCB2QwYAAAAAAAAAAAAAAAAAAAAAAAAAAAADsxmwAAAAAAAAAAAAAAAAAAAAAAAAAAAAHBgNgMGAAAAAAAAAAAAAAAAAAAAAAAAAACAA7MZMAAAAAAAAAAAAAAAAAAAAAAAAAAAAByYzYABAAAAAAAAAAAAAAAAAAAAAAAAAADgwGwGDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdmM2AAAAAAAAAAAAAAAAAAAAAAAAAAAAA4MJsBAwAAAAAAAAAAAAAAAAAAAAAAAAAAwIHZDBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAOzGbAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcGA2AwYAAAAAAAAAAAAAAAAAAAAAAAAAAIADsxkwAAAAAAAAAAAAAAAAAAAAAAAAAAAAHJjNgAEAAAAAAAAAAAAAAAAAAAAAAAAAAODAbAYMAAAAAAAAAAAAAAAAAAAAAAAAAAAAB2YzYAAAAAAAAAAAAAAAAAAAAAAAAAAAADgwmwEDAAAAAAAAAAAAAAAAAAAAAAAAAADAgdkMGAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7MZsAAAAAAAAAAAAAAAAAAAAAAAAAAAABwYDYDBgAAAAAAAAAAAAAAAAAAAAAAAAAAgAOzGTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcmM2AAQAAAAAAAAAAAAAAAAAAAAAAAAAA4MBsBgwAAAAAAAAAAAAAAAAAAAAAAAAAAAAHZjNgAAAAAAAAAAAAAAAAAAAAAAAAAAAAODCbAQMAAAAAAAAAAAAAAAAAAAAAAAAAAMCB2QwYAAAAAAAAAAAAAAAAAAAAAAAAAAAADsxmwAAAAAAAAAAAAAAAAAAAAAAAAAAAAHBgNgMGAAAAAAAAAAAAAAAAAAAAAAAAAACAA7MZMAAAAAAAAAAAAAAAAAAAAAAAAAAAAByYzYAB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AAAAAAAAAAAAAAAAcGA2AwYAAAAAAAAAAAAAAAAAAAAAAAAAAIADsxkwAAAAAAAAAAAAAAAAAAAAAAAAAAAAHJjNgAEAAAAAAAAAAAAAAAAAAAAAAAAAAODAbAYMAAAAAAAAAAAAAAAAAAAAAAAAAAAAB2YzYAAAAAAAAAAAAAAAAAAAAAAAAAAAADgwmwEDAAAAAAAAAAAAAAAAAAAAAAAAAADAgdkMGAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7MZsAAAAAAAAAAAAAAAAAAAAAAAAAAAABwYDYDBgAAAAAAAAAAAAAAAAAAAAAAAAAAgAOzGTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcmM2AAQAAAAAAAAAAAAAAAAAAAAAAAAAA4MBsBgwAAAAAAAAAAAAAAAAAAAAAAAAAAAAHZjNgAAAAAAAAAAAAAAAAAAAAAAAAAAAAODCbAQMAAAAAAAAAAAAAAAAAAAAAAAAAAMCB2QwYAAAAAAAAAAAAAAAAAAAAAAAAAAAADsxmwAAAAAAAAAAAAAAAAAAAAAAAAAAAAHBgNgMGAAAAAAAAAAAAAAAAAAAAAAAAAACAA7MZMAAAAAAAAAAAAAAAAAAAAAAAAAAAAByYzYABAAAAAAAAAAAAAAAAAAAAAAAAAADgwGwGDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdmM2AAAAAAAAAAAAAAAAAAAAAAAAAAAAA4MJsBAwAAAAAAAAAAAAAAAAAAAAAAAAAAwIHZDBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAOzGbAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcGA2AwYAAAAAAAAAAAAAAAAAAAAAAAAAAIADsxkwAAAAAAAAAAAAAAAAAAAAAAAAAAAAHJjNgAEAAAAAAAAAAAAAAAAAAAAAAAAAAODAbAYMAAAAAAAAAAAAAAAAAAAAAAAAAAAAB2YzYAAAAAAAAAAAAAAAAAAAAAAAAAAAADgwmwEDAAAAAAAAAAAAAAAAAAAAAAAAAADAgdkMGAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7MZsAAAAAAAAAAAAAAAAAAAAAAAAAAAABwYDYDBgAAAAAAAAAAAAAAAAAAAAAAAAAAgAOzGTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcmM2AAQAAAAAAAAAAAAAAAAAAAAAAAAAA4MBsBgwAAAAAAAAAAAAAAAAAAAAAAAAAAAAHZjNgAAAAAAAAAAAAAAAAAAAAAAAAAAAAODCbAQMAAAAAAAAAAAAAAAAAAAAAAAAAAMCB2QwYAAAAAAAAAAAAAAAAAAAAAAAAAAAADsxmwAAAAAAAAAAAAAAAAAAAAAAAAAAAAHBgNgMGAAAAAAAAAAAAAAAAAAAAAAAAAACAA7MZMAAAAAAAAAAAAAAAAAAAAAAAAAAAAByYzYABAAAAAAAAAAAAAAAAAAAAAAAAAADgwGwGDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdmM2AAAAAAAAAAAAAAAAAAAAAAAAAAAAA4MJsBAwAAAAAAAAAAAAAAAAAAAAAAAAAAwIHZDBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAOzGbAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcGA2AwYAAAAAAAAAAAAAAAAAAAAAAAAAAIADsxkwAAAAAAAAAAAAAAAAAAAAAAAAAAAAHJjNgAEAAAAAAAAAAAAAAAAAAAAAAAAAAODAbAYMAAAAAAAAAAAAAAAAAAAAAAAAAAAAB2YzYAAAAAAAAAAAAAAAAAAAAAAAAAAAADgwmwEDAAAAAAAAAAAAAAAAAAAAAAAAAADAgdkMGAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7MZsAAAAAAAAAAAAAAAAAAAAAAAAAAAABwYDYDBgAAAAAAAAAAAAAAAAAAAAAAAAAAgAOzGTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcmM2AAQAAAAAAAAAAAAAAAAAAAAAAAAAA4MBsBgwAAAAAAAAAAAAAAAAAAAAAAAAAAAAHZjNgAAAAAAAAAAAAAAAAAAAAAAAAAAAAODCbAQMAAAAAAAAAAAAAAAAAAAAAAAAAAMCB2QwYAAAAAAAAAAAAAAAAAAAAAAAAAAAADsxmwAAAAAAAAAAAAAAAAAAAAAAAAAAAAHBgNgMGAAAAAAAAAAAAAAAAAAAAAAAAAACAA7MZMAAAAAAAAAAAAAAAAAAAAAAAAAAAAByYzYABAAAAAAAAAAAAAAAAAAAAAAAAAADgwGwGDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdmM2AAAAAAAAAAAAAAAAAAAAAAAAAAAAA4MJsBAwAAAAAAAAAAAAAAAAAAAAAAAAAAwIHZDBgAAAAAAAAA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\n",
      "text/plain": [
       "<Figure size 7200x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.rcParams[\"figure.figsize\"] = (100,10)\n",
    "y_compare.plot(y=['실제 방문객 수', '예측 방문객 수'], kind=\"bar\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "70b549a7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x1080 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt \n",
    "import seaborn as sns   \n",
    "\n",
    "plt.figure(figsize=(15,15))\n",
    "sns.heatmap(data = y_compare.corr(), annot=True, \n",
    "fmt = '.2f', linewidths=5, cmap='Reds')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce7bd726",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
