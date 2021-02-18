{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "extended-quarter",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What is the salesperson's name?  Alice jayne\n",
      "What were their sales? 5600\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Alice jayne earned a bonus of 100\n",
      "as well as 2 Days off!\n"
     ]
    }
   ],
   "source": [
    "salesname=input(\"What is the salesperson's name? \")\n",
    "salestotal=int(input(\"What were their sales?\") )\n",
    "if(salestotal<5000):\n",
    "    bonus=0\n",
    "    daysOff=0\n",
    "else:\n",
    "    bonus =100\n",
    "    daysOff=2\n",
    "print(salesname,\"earned a bonus of\",bonus)\n",
    "print('as well as', daysOff,'Days off!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "therapeutic-citation",
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
   "version": "3.9.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
