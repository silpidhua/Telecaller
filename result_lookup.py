import pymysql

class Results:

    db = None
    def __init__(self):
        try:
            self.db = pymysql.connect("remotemysql.com", "oKtWb3PkkW", "3E6PejX7zR", "oKtWb3PkkW", 3306)
            print("db connected")
        except:
            print("Failed in DB connection")
            self.db.close()

    def getResult(self,phone_num):
        try:
            cursor = self.db.cursor()
            query = "select marks from telecomeresult where contactno = \'" + phone_num + "\'"
            print(query)
            cursor.execute(query)
            record = cursor.fetchone()
            print(record)
            cursor.close()
            marks = record[0]
            #  marks = get result from executing query
            if marks is not None:
                return marks
            else:
                return 'not found'
        except Exception as ex:
            print(ex)
            print("Failed to read data from table")
            self.db.close()

if __name__ == "__main__":
    result = Results()
    print(result.getResult('08123716322'))