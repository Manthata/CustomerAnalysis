const express = require("express");
const router = express.Router();
const rootDir = require("../utils/path");
const path = require("path");
const videocontroler = require("../controlers/videocontroler")
const datacontroler = require("../controlers/dataControler")

//Get for adding products and eddint products 
router.get("/", datacontroler.gethome);
router.get("/live", videocontroler.getVideo);
// router.get("/admin/edit-products/:productId", ProductControler.getEditProducts);
// router.get("/admin/products", ProductControler.getProducts);

// // router.get("", ProductControler.getAdminProducts);

// router.post("/admin/add-products", ProductControler.postAddProducts)
// router.post("/admin/edit-products", ProductControler.postEditProduct);
// router.post("/admin/delete-product", ProductControler.postDeleteProduct )


// // router.post("/admin/edit-products", ProductControler.postAddProducts);
// router.post("/admin/edit-products/:productId", ProductControler.getEditProducts)

module.exports = router;
