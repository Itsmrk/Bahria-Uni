{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number : 3\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "temp = 1\n",
    "num = int(input(\"Enter a number : \"))\n",
    "a =1\n",
    "while a <= num:\n",
    "    temp *=a\n",
    "    a+=1\n",
    "print(temp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "temp = 1\n",
    "num = int(input(\"Enter a number : \"))\n",
    "a=list(range(num+1))[1:]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4 3 2 1 "
     ]
    }
   ],
   "source": [
    "mylist = [1,2,3,4]\n",
    "lislen = len(mylist)\n",
    "while a <= lislen:\n",
    "    print(mylist[lislen-1],end=' ')\n",
    "    lislen -=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4 3 2 1 "
     ]
    }
   ],
   "source": [
    "mylist = [1,2,3,4]\n",
    "lislen = len(mylist)\n",
    "for a in range(lislen):\n",
    "    print(mylist[lislen-1],end=' ')\n",
    "    lislen -=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter number to add in list1\n",
      "Enter number to add in list2\n",
      "Enter number to add in list3\n",
      "Enter number to add in list4\n",
      "Enter number to add in list5\n",
      "Enter a number to delete from list5\n",
      "value found\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "newlist=[]\n",
    "for i in range(5):\n",
    "    newlist.append(int(input(\"Enter number to add in list : \")))\n",
    "delnum = int(input(\"Enter a number to delete from list : \"))\n",
    "for i in range(5):\n",
    "    if (newlist[i] == delnum):\n",
    "        print(\"value found\")\n",
    "        newlist.remove(delnum)\n",
    "        break\n",
    "newlist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
