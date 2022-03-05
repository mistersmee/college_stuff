{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "88a6fe6e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2.2, 'kit']\n"
     ]
    }
   ],
   "source": [
    "a = [1, 2.2, 'kit']\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "452c4d6b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.2\n"
     ]
    }
   ],
   "source": [
    "print(a[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c10992cc",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "At index 0,element is 1\n",
      "At index 1,element is 2.2\n",
      "At index 2,element is 5.5\n",
      "At index 3,element is 6.6\n",
      "At index 4,element is abc\n",
      "At index 5,element is xyz\n"
     ]
    }
   ],
   "source": [
    "s = [1, 2.2, 5.5, 6.6, 'abc', 'xyz']\n",
    "i = 0\n",
    "while i < len(s):\n",
    "    print(f'At index {i},element is {s[i]}')\n",
    "    i += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0fb1f8cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2.2\n",
      "5.5\n",
      "6.6\n",
      "abc\n",
      "xyz\n"
     ]
    }
   ],
   "source": [
    "for i in s:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6b34a28b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "4\n",
      "9\n",
      "16\n",
      "25\n",
      "36\n",
      "49\n",
      "64\n"
     ]
    }
   ],
   "source": [
    "a = [1, 2, 3, 4, 5, 6, 7, 8]\n",
    "for i in a:\n",
    "    sq = i * i\n",
    "    print(sq)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a7dd3a90",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['p', 'y', 't', 'h', 'o', 'n']\n"
     ]
    }
   ],
   "source": [
    "s = ['p', 'y', 't', 'h', 'o', 'n']\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "13f9ab8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['y', 't']\n"
     ]
    }
   ],
   "source": [
    "print(s[1:3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "5cc19173",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['t', 'h', 'o', 'n']\n"
     ]
    }
   ],
   "source": [
    "print(s[2:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "bd102f7f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['p']\n"
     ]
    }
   ],
   "source": [
    "print(s[:-5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "0fb78e04",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['p', 'y', 't', 'h', 'o', 'n']\n"
     ]
    }
   ],
   "source": [
    "print(s[:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "4ce9446f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['n', 'o', 'h', 't', 'y', 'p']\n"
     ]
    }
   ],
   "source": [
    "print(s[::-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "6251650a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['p', 'y', 't', 'h', 'o', 'n', 122, 122]\n"
     ]
    }
   ],
   "source": [
    "s.append(122)\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "367c5963",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = ['zoo', 'star']\n",
    "i = 1\n",
    "while i <= 5:\n",
    "    value = input()\n",
    "    a.append(value)\n",
    "    i += 1\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1141bad3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['English', 'Maths', 'Marathi', 'Science']\n",
      "['English', 'Maths', 'Hindi', 'Marathi', 'Science']\n",
      "['English', 'Maths', 'Hindi', 'History', 'Marathi', 'Science']\n"
     ]
    }
   ],
   "source": [
    "subject = ['English', 'Maths', 'Marathi', 'Science']\n",
    "print(subject)\n",
    "subject.insert(2,'Hindi')\n",
    "print(subject)\n",
    "subject.insert(3,'History')\n",
    "print(subject)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "151d41c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Before using the extend function, list 1 is: [10, 20, 30]\n",
      "After using the extend function, list 2 is: [10, 20, 30, 15, 35, 77, 88, 90]\n"
     ]
    }
   ],
   "source": [
    "list1 = [10, 20, 30]\n",
    "list2 = [15, 35, 77, 88, 90]\n",
    "print(f'Before using the extend function, list 1 is: {list1}')\n",
    "list1.extend(list2)\n",
    "print(f'After using the extend function, list 2 is: {list1}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ef31e751",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['p', 'y', 't', 'h', 'o', 'n']\n",
      "['p', 't', 'h', 'o', 'n']\n",
      "['p', 't', 'h', 'o']\n",
      "[]\n"
     ]
    }
   ],
   "source": [
    "s = ['p', 'y', 't', 'h', 'o', 'n']\n",
    "print(s)\n",
    "del(s[1])\n",
    "print(s)\n",
    "s.pop()\n",
    "print(s)\n",
    "s.clear()\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "d995bd1a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 4, 5, 12, 22, 66]\n",
      "[66, 22, 12, 5, 4, 2, 1]\n"
     ]
    }
   ],
   "source": [
    "s = [22, 1, 5, 4, 2, 66, 12]\n",
    "s.sort()\n",
    "print(s)\n",
    "s.reverse()\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "a7fcc851",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "[22, 33, 44, 55, 66, 77, 88, 99]\n"
     ]
    }
   ],
   "source": [
    "t = [22, 33 , 44, 55, 66, 77, 88, 99]\n",
    "print(t.index(88))\n",
    "print(t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "925919c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "20\n",
      "[30, 49, 88]\n",
      "7\n",
      "['kit', 'coek']\n"
     ]
    }
   ],
   "source": [
    "list3 = [10, 20, [30, 49, 88], 7, ['kit', 'coek']]\n",
    "for i in list3:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f51cd653",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "4045ad01",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "20\n",
      "[30, 49, 88]\n",
      "7\n",
      "['kit', 'coek']\n",
      "[10, 20, [30, 49, 88], 7, ['kit', 'coek']]\n",
      "49\n",
      "88\n",
      "coek\n"
     ]
    }
   ],
   "source": [
    "list3 = [10, 20, [30, 49, 88], 7, ['kit', 'coek']]\n",
    "i = 0\n",
    "while i < len(list3):\n",
    "    print(list3[i])\n",
    "    i += 1\n",
    "print(list3)\n",
    "print(list3[2][1])\n",
    "print(list3[2][2])\n",
    "print(list3[4][1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "4d4e0dfe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Element absent.\n",
      "Element absent.\n",
      "Element absent.\n",
      "Element absent.\n",
      "Element present.\n",
      "Element absent.\n",
      "Element present.\n"
     ]
    }
   ],
   "source": [
    "test = [1, 6, 3, 5, 4, 2]\n",
    "for i in test:\n",
    "    if i == 4:\n",
    "        print('Element present.')\n",
    "    else:\n",
    "        print('Element absent.')\n",
    "        \n",
    "if 4 in test:\n",
    "    print('Element present.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "04976d36",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6, 7]\n",
      "[]\n",
      "[1, 2, 3, 4, 5, 6, 7]\n"
     ]
    }
   ],
   "source": [
    "list1 = [1, 2, 3, 4, 5, 6, 7]\n",
    "list2 = list1.copy()\n",
    "print(list2)\n",
    "list2.clear()\n",
    "print(list2)\n",
    "list2 += list1\n",
    "print(list2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "0bd664c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 0, 0, 0, 0]\n"
     ]
    }
   ],
   "source": [
    "numbers = [0] * 5\n",
    "print(numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "8d8c63f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('apple', 'banana', 'cherry')\n",
      "('abc', 34, True, 40, 'male')\n",
      "()\n",
      "('python', 'geeks')\n",
      "(0, 1, 2, 3, 'python', 'geek')\n",
      "((0, 1, 2, 3), ('python', 'geek'))\n",
      "(1, 2, 3)\n",
      "(3, 2, 1, 0)\n",
      "(2, 3)\n",
      "2\n",
      "Yes, 'apple' is in the fruits tuple\n"
     ]
    }
   ],
   "source": [
    "thistuple = (\"apple\", \"banana\", \"cherry\")\n",
    "print(thistuple)\n",
    "\n",
    "tuple1 = (\"abc\", 34, True, 40, \"male\")\n",
    "print(tuple1)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "# An empty tuple\n",
    "empty_tuple = ()\n",
    "print (empty_tuple)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "# Creating non-empty tuples\n",
    " \n",
    "tup = ('python', 'geeks')\n",
    "print(tup)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "# Code for concatenating 2 tuples\n",
    " \n",
    "tuple1 = (0, 1, 2, 3)\n",
    "tuple2 = ('python', 'geek')\n",
    " \n",
    "# Concatenating above two\n",
    "print(tuple1 + tuple2)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "# Code for creating nested tuples\n",
    " \n",
    "tuple1 = (0, 1, 2, 3)\n",
    "tuple2 = ('python', 'geek')\n",
    "tuple3 = (tuple1, tuple2)\n",
    "print(tuple3)\n",
    "\n",
    "\n",
    "# code to test slicing\n",
    " \n",
    "tuple1 = (0 ,1, 2, 3)\n",
    "print(tuple1[1:])\n",
    "print(tuple1[::-1])\n",
    "print(tuple1[2:4])\n",
    "\n",
    "# Code for printing the length of a tuple\n",
    " \n",
    "tuple2 = ('python', 'geek')\n",
    "print(len(tuple2))\n",
    "\n",
    "\n",
    "thistuple = (\"apple\", \"banana\", \"cherry\")\n",
    "if \"apple\" in thistuple:\n",
    "  print(\"Yes, 'apple' is in the fruits tuple\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "52ea65ac",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "At index 0,element is 1\n",
      "At index 1,element is 2.2\n",
      "At index 2,element is 5.5\n",
      "At index 3,element is 6.6\n",
      "At index 4,element is abc\n",
      "At index 5,element is xyz\n"
     ]
    }
   ],
   "source": [
    "s = [1, 2.2, 5.5, 6.6, 'abc', 'xyz']\n",
    "for i  in range(len(s)):\n",
    "    print(f'At index {i},element is {s[i]}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "55285aed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3]\n",
      "('one', 'two', 'three')\n"
     ]
    }
   ],
   "source": [
    "number_tuple = (1, 2, 3)\n",
    "number_list = list(number_tuple)\n",
    "print(number_list)\n",
    "str_list = ['one', 'two', 'three']\n",
    "str_tuple = tuple(str_list)\n",
    "print(str_tuple)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "8e1561f0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}\n",
      "Ford\n",
      "at key brand value is Ford\n",
      "at key model value is Mustang\n",
      "at key year value is 1964\n",
      "{1: 100, 2: 20, 3: 30}\n"
     ]
    }
   ],
   "source": [
    "\n",
    "thisdict = {\n",
    "  \"brand\": \"Ford\",\n",
    "  \"model\": \"Mustang\",\n",
    "  \"year\": 1964\n",
    "}\n",
    "print(thisdict)\n",
    "\n",
    "thisdict = {\n",
    "  \"brand\": \"Ford\",\n",
    "  \"model\": \"Mustang\",\n",
    "  \"year\": 1964\n",
    "}\n",
    "print(thisdict[\"brand\"])\n",
    "\n",
    "for i in thisdict:\n",
    "    print(f'at key {i} value is {thisdict[i]}')\n",
    "\n",
    "d = {1:10, 2:20, 3:30}\n",
    "d[1] = 100\n",
    "print(d)"
   ]
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
