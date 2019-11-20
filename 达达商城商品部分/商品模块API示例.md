

# 商品模块-接口说明

### 流程说明：

商品首页展示 - 在商城首页的下半部为商品部分展示，在首页展示的效果为每个品类下展示三个该品类的商品，如果每个类别下的sku不足三个会报错，这一点需注意。

商品品类页展示 - 根据商品的不同分类进行相应的展示，具有分页展示的功能。

商品详情页展示 - 为确定到某一个 sku 需要在商品详情页选择相关的属性来确定库存项。

商品首页搜索 - 根据 spu 的 name 字段进行查询，具有分页展示功能。

### 一，首页商品展示

**URL：**`127.0.0.1:8000/v1/carts/<username>`

**请求方式**：GET

**返回值：**JSON

| 字段                             | 含义                         | 类型 | 备注          |
| -------------------------------- | ---------------------------- | ---- | ------------- |
| code                             | 状态                         | int  | 默认正常为200 |
| data(以下数据均为data下的子数据) | 返回具体的数据都包含在data中 | {}   |               |
| catalog_id                       | 品类id                       | int  |               |
| catalog_name                     | 品类名称                     | str  |               |
| sku                              | 该列表下为商品具体数据       |      |               |
| skuid                            | skuid                        | int  |               |
| name                             | sku商品标题                  | str  |               |
| caption                          | sku副标题                    | str  |               |
| price                            | sku价格                      | str  |               |
| image                            | sku图片                      | str  |               |

**响应格式**：

```python
#响应
{
    "code": 200,
    "data": [
        {
            "catalog_id": 1,
            "catalog_name": "leg beg",
            "sku": [
                {
                    "skuid": 1,
                    "caption": "sku_caption_1",
                    "name": "sku_name_1",
                    "price": "1.00",
                    "image": "1_oZtCaDx.jpg"
                },
                {
                    "skuid": 2,
                    "caption": "sku_name_2_cap",
                    "name": "sku_name_2",
                    "price": "22.00",
                    "image": "v2-b01fad0ef311933a6308c14b2a00a35e_r_PptidVI.jpg"
                },
                {
                    "skuid": 3,
                    "caption": "sku_name_3_cap",
                    "name": "sku_name_3",
                    "price": "123213.00",
                    "image": "1_Pa1gqJJ.jpg"
                }
            ]
        },
        {
            "catalog_id": 2,
            "catalog_name": "cata02",
            "sku": [
                {
                    "skuid": 4,
                    "caption": "sku_name_4_cap",
                    "name": "sku_name_4",
                    "price": "1.00",
                    "image": "v2-b01fad0ef311933a6308c14b2a00a35e_r_KRSDFlj.jpg"
                },
                {
                    "skuid": 5,
                    "caption": "sku_name_5_cap",
                    "name": "sku_name_5",
                    "price": "1.00",
                    "image": "v2-b01fad0ef311933a6308c14b2a00a35e_r_CgEk10d.jpg"
                },
                {
                    "skuid": 14,
                    "caption": "test111",
                    "name": "test111",
                    "price": "1.00",
                    "image": "v2-b01fad0ef311933a6308c14b2a00a35e_r_b8Ek59E.jpg"
                }
            ]
        }
    ]
}
```

**状态码参考**：

| 状态码 | 响应信息   | 原因短语 |
| ------ | ---------- | -------- |
| 200    | 正常       | OK       |
| 500    | 未找到商品 |          |



### 二，获取商品品类页接口

**URL：**`127.0.0.1:8000/v1/goods/catalogs/<catalog_id>/`

**请求方式:** GET

**请求参数：**

**URL：**`127.0.0.1:8000/v1/goods/catalogs/<catalog_id>?launched=true&page=1&pagesize=3`

| 字段     | 含义                 | 类型 | 备注       |
| -------- | -------------------- | ---- | ---------- |
| launched | 该sku是否上线        | str  | 默认为true |
| page     | 分页项的当前页参数   | int  |            |
| pagesize | 每页所展示数据的数量 | int  |            |

**返回值：**JSON

**响应格式**：

```python
#响应示例：
{
    "code": 200,
    "data": [
        {
            "skuid": 1,
            "name": "sku_name_1",
            "price": "1.00",
            "image": "1_oZtCaDx.jpg"
        },
        {
            "skuid": 2,
            "name": "sku_name_2",
            "price": "22.00",
            "image": "v2-b01fad0ef311933a6308c14b2a00a35e_r_PptidVI.jpg"
        },
        {
            "skuid": 3,
            "name": "sku_name_3",
            "price": "123213.00",
            "image": "1_Pa1gqJJ.jpg"
        },
        {
            "skuid": 6,
            "name": "sku_name_6",
            "price": "1.00",
            "image": "1_meW4pX7.jpg"
        },
        {
            "skuid": 7,
            "name": "test1",
            "price": "1.00",
            "image": "v2-b01fad0ef311933a6308c14b2a00a35e_r_v7tFz6E.jpg"
        },
        {
            "skuid": 8,
            "name": "test2",
            "price": "1.00",
            "image": "v2-b01fad0ef311933a6308c14b2a00a35e_r_6BiraZa.jpg"
        },
        {
            "skuid": 9,
            "name": "test3",
            "price": "1.00",
            "image": "1_XAOOXgX.jpg"
        },
        {
            "skuid": 10,
            "name": "test4",
            "price": "1.00",
            "image": "v2-b01fad0ef311933a6308c14b2a00a35e_r_vOrRHZY.jpg"
        },
        {
            "skuid": 11,
            "name": "test5",
            "price": "1.00",
            "image": "v2-b01fad0ef311933a6308c14b2a00a35e_r_hofJAkI.jpg"
        }
    ],
    "paginator": {
        "pagesize": 9,
        "total": 12
    }
}
```

| 字段     | 含义       | 类型 | 备注                        |
| -------- | ---------- | ---- | --------------------------- |
| code     | 状态码     | int  | 默认正常为200，异常见状态码 |
| data     | 具体数据   | dict | 与error二选一               |
| error    | 错误信息   | char | 与data二选一                |
| base_url | 图片根路径 | str  |                             |

**data参数信息**

| 参数  | 类型 | 是否必须 |       说明       |
| :---: | :--: | :------: | :--------------: |
| skuid | int  |    是    |    商品sku_id    |
| name  | str  |    是    |     商品名称     |
| price | int  |    是    |     商品价格     |
| image | str  |    是    | 商品默认图片路径 |

**状态码参考**

| 状态码 | 响应信息                      | 原因短语                      |
| ------ | ----------------------------- | ----------------------------- |
| 200    | 正常                          | OK                            |
| 40200  | 页数有误，小于0或者大于总页数 | 页数有误，小于0或者大于总页数 |



### 三，商品详情页展示

**URL：**`127.0.0.1:8000/v1/goods/detail/<sku_id>/`

**请求方式**：GET

**返回值**：JSON

**响应格式：**

```python
#响应示例
{
    "code": 200,
    "data": {
        "image": "1_oZtCaDx.jpg",
        "spu": 1,
        "name": "sku_name_1",
        "caption": "sku_caption_1",
        "price": "1.00",
        "catalog_id": 1,
        "catalog_name": "leg beg",
        "sku_sale_attr_id": [
            5,
            4
        ],
        "sku_sale_attr_names": [
            "weight",
            "color"
        ],
        "sku_sale_attr_val_id": [
            5,
            3
        ],
        "sku_sale_attr_val_names": [
            "100",
            "red"
        ],
        "sku_all_sale_attr_vals_id": {
            "5": [
                5,
                6
            ],
            "4": [
                3,
                4
            ]
        },
        "sku_all_sale_attr_vals_name": {
            "5": [
                "100",
                "200"
            ],
            "4": [
                "red",
                "black"
            ]
        }
    }
}
```

| 字段                        | 含义                               | 类型 | 备注           |
| --------------------------- | ---------------------------------- | ---- | -------------- |
| code                        | 状态                               | Int  | 正常为200      |
| data                        | 返回的具体数据均在data里           | {}   | 数据格式见上图 |
| image                       | sku图片                            | str  |                |
| spu                         | 该sku所对应的spu                   | int  |                |
| name                        | sku正标题                          | str  |                |
| caption                     | sku副标题                          | str  |                |
| price                       | sku销售价                          | str  |                |
| catalog_id                  | 类别id                             | int  |                |
| catalog_name                | 类别名称                           | str  |                |
| sku_sale_attr_id            | 该sku所具备的销售属性id            | list |                |
| sku_sale_attr_names         | 该sku所具备的销售属性名称          | list |                |
| sku_sale_attr_val_id        | sku销售属性值id                    | list |                |
| sku_sale_attr_val_name      | sku销售属性值名称                  | list |                |
| sku_all_sale_attr_vals_id   | 每个销售所对应的所有销售属性值id   | dict |                |
| sku_all_sale_attr_vals_name | 每个销售所对应的所有销售属性值名称 | dict |                |



**状态码参考**

| 状态码 | 响应信息     | 原因短语              |
| ------ | ------------ | --------------------- |
| 200    | 正常         | OK                    |
| 40201  | sku_id不存在 | Such sku doesn' exist |



### 四，商品首页搜索

**URL：**`127.0.0.1:8000/v1/goods/search`

**请求方式**：POST

**返回值**：JSON

**响应格式：**

```python
#响应示例：
{
    "code": 200,
    "data": [
        {
            "skuid": 4,
            "name": "sku_name_4",
            "price": "1.00",
            "image": "v2-b01fad0ef311933a6308c14b2a00a35e_r_KRSDFlj.jpg"
        },
        {
            "skuid": 5,
            "name": "sku_name_5",
            "price": "1.00",
            "image": "v2-b01fad0ef311933a6308c14b2a00a35e_r_CgEk10d.jpg"
        },
        {
            "skuid": 14,
            "name": "test111",
            "price": "1.00",
            "image": "v2-b01fad0ef311933a6308c14b2a00a35e_r_b8Ek59E.jpg"
        }
    ],
    "paginator": {
        "pagesize": 9,
        "total": 3
    }
}
```

| 字段      | 含义                     | 类型 | 备注               |
| --------- | ------------------------ | ---- | ------------------ |
| code      | 状态                     | Int  | 正常为200          |
| data      | 返回的具体数据均在data里 | {}   | 相应格式数据见下图 |
| skuid     | skuid                    | int  |                    |
| name      | sku正标题                | str  |                    |
| price     | sku销售价                | str  |                    |
| image     | sku图片                  | str  |                    |
| paginator | 分页参数                 | {}   |                    |
| pagesize  | 每页显示条目数量         | int  |                    |
| total     | 总计数据量               | int  |                    |

**状态码参考**

| 异常码 | 含义      | 备注                          |
| ------ | --------- | ----------------------------- |
| 40200  | 分页有误  | 页数有误，小于0或者大于总页数 |
| 40202  | sku不存在 | 您所查询的商品不存在          |



### 五，详情页 SKU 切换

**URL：**`127.0.0.1:8000/v1/goods/sku`

**请求方式**：POST

**返回值**：JSON

**响应格式：**

```python
#响应示例：
{
    "code": 200,
    "data": 1
}
```

| 字段 | 含义    | 类型 | 备注      |
| :--- | ------- | ---- | --------- |
| code | 状态    | Int  | 正常为200 |
| data | sku的id | int  |           |

**状态码参考**

| 异常码 | 含义      | 备注                 |
| ------ | --------- | -------------------- |
| 200    | 分页有误  |                      |
| 40050  | sku不存在 | 您所查询的商品不存在 |

