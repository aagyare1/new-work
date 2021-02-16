{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "northern-replication",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Fran's Place!\n",
      "\n",
      "\n",
      "Let's proceed to checkout!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "How many candy bars did they buy? 4\n",
      "How  many energy drinks di they buy?  6\n",
      "How  many gallons of gas  did they buy? 12\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "Item       Qnt     Total\n",
      "---------------------------------\n",
      "Candy 4 $5.00\n",
      "Drinks 6 $13.50\n",
      "Gas 12 $34.55\n",
      "---------------------------------\n",
      "Subtotal  $53.05\n",
      "Tax       $3.85\n",
      "Total     $56.89\n",
      "\n",
      "\n",
      "HAVE A GREAT DAY \n"
     ]
    }
   ],
   "source": [
    "print(\"Welcome to Fran's Place!\\n\\n\")\n",
    "print(\"Let's proceed to checkout!\")\n",
    "\n",
    "candy = int (input (\"How many candy bars did they buy?\"))\n",
    "drinks = int( input (\"How  many energy drinks di they buy? \"))\n",
    "gas= int (input(\"How  many gallons of gas  did they buy?\"))\n",
    "\n",
    "candytotal=candy* 1.25\n",
    "drinktotal=drinks * 2.25\n",
    "gastotal=gas* 2.879\n",
    "subtotal= candytotal+drinktotal+gastotal\n",
    "tax= subtotal * .0725;\n",
    "\n",
    "print(\"\\n\\nItem       Qnt     Total\")\n",
    "print(\"---------------------------------\")\n",
    "print(\"Candy\",  candy,  \"$%.2f\" % candytotal)\n",
    "print(\"Drinks\", drinks, \"$%.2f\" % drinktotal)\n",
    "print(\"Gas\",    gas,    \"$%.2f\" % gastotal)\n",
    "\n",
    "print(\"---------------------------------\")\n",
    "print(\"Subtotal  $%.2f\" %subtotal)\n",
    "print(\"Tax       $%.2f\" %tax)\n",
    "print(\"Total     $%.2f\" %(subtotal + tax))\n",
    "print (\"\\n\\nHAVE A GREAT DAY \")\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "technical-worth",
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
