import express from 'express';
import redis from 'redis;
import { promisify } from 'util';

const app = express();
const client = redis.createClient();
const PORT = 1245;

const get = promisify(client.get).bind(client);

const listProducts = [
  {itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4},
  {itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10},
  {itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2},
  {itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5},
];

function getItemById(id) {
  for (let product of listProducts) {
    if (id === product.itemId) {
      return product;
    }
  }
}

function reserveStockById(itemId, stock) {
  const itemName = `item.${itemId}`;
  client.set(itemName, stock, redis.print);
}

async function getCurrentReservedStockById(itemId) {
  const itemName = `item.${itemId}`;
  const stock = await get(itemName);
  return stock;
}

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', (req, res) => {
  const id = req.params.itemId;
  const item = getItemById(parseInt(id));
});

app.listen(PORT);

