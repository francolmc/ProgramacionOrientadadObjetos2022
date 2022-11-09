class Product:
    def __init__(self):
        self._id = 0
        self._productName = ''
        self._price = 0
        self._createdAt = ''
        self._updatedAt = ''

    def getId(self) -> int:
        return self._id

    def getProductName(self) -> str:
        return self._productName

    def setProductName(self, value: str):
        self._productName = value

    def getPrice(self) -> int:
        return self._price

    def setPrice(self, value: int):
        self._price = value

    def getCreatedAt(self) -> str:
        return self._createdAt

    def getUpdatedAt(self) -> str:
        return self._updatedAt

    def insertSQL(self):
        return f"INSERT INTO product (productName, price) VALUES ('{self._productName}', '{self._price}')"

    def updateSQL(self):
        return f"UPDATE product SET productName='{self._productName}', price='{self._price}' WHERE"

    def deleteSQL(self):
        return f"DELETE FROM product WHERE id={self._id}"

    def selectOneRecordSQL(self, id: int):
        return f"SELECT id, productName, price, createdAt, updatedAt FROM product WHERE id = '{id}'"