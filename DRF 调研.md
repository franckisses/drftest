### DRF 调研：

## API：

###Request ：

​		REST framwork 中的request扩展自标准的HTTPRequest.提供了一种比较灵活的请求解析和请求认证功能。

 #### Request.data ：

​		封装了request.POST和request.File ,不止支持forming data的提交，也支持文件等操作。可以使用传入表单还是传入json数据，都可以通过.data来解析。 （支持解析除POST以外的其他方法）

```python
# 前端请求为：http://127.0.0.1:8000/v1/users/index?name=test
# 请求方法为：POST

# 后端代码为：
from rest_framework import.views import APIview

class Index(APIView):
		def get(self,request):
    		print(request)
        print(request.data,type(request.data))
        print(request.query_params['name'])
        return Response({'code':200})
   
    def post(self,request):
        print(request.data)
        print(request.query_params)
        return Response({'code':200})

    def put(self,request):
        print(request.data)
        return Response({'code':200})

    def delete(self,request):
        print(request.data)
        return Response({'code':200})
# POST 打印结果：
# {'name': 'root', 'password': 'baidu'}  type:dict
# <QueryDict: {'name': ['test']}>

# GET 打印结果：
# <rest_framework.request.Request object at 0x111cb1390>
# {'name': 'root', 'password': 'baidu'} type:dict

# PUT 打印结果
# {'name': 'root', 'password': 'baidu'} type:dict

# DELETE 打印结果
# {'name': 'root', 'password': 'baidu'} type:dict

```





 #### Request.query_params :

​		 使用query_params，用来获取查询字符串，因为不止request.get可以获得查询字符串。其他请求的方式也可以使用此属性来获取查询字符串。 

#### Request.parsers: 

![drf_process](drf_process.png)



​           如果用户通过传入到一个不能解析的内容。通过访问可能回抛出ParserError,如果使用APIView，或者使用@api_view装饰器能够捕获这种错误，返回`400 （Bad Request）`错误。   

​		如果客户端发送的请求内容无法解析（不同于格式错误），则会引发 `UnsupportedMediaType` 异常，默认情况下会被捕获并返回 `415 Unsupported Media Type` 响应。

#### Authentication：

​		REST framwork 提供一个灵活，每一次请求的认证。提供了以下的功能：

> 对于不同的API，提供不同的认证机制。
>
> 提供多种不同的身份认证机制。 
>
> 提供传入请求和不同的令牌的请求。   

#### Request.user

​			request.user 通常返回`django.contrib.auth.models.User`的实例 ,尽管依赖于当前的用户的认证策略。

​	       request.auth 如果没有认证的话，则返回的是`django.contrib.auth.models.AnonymousUser`.

#### Request.auth

​		`request.auth` 返回任何条件下的请求认证上下文，确切的来说是依赖与已经应用的认证策略`request.auth`。通常上来说经过身份认证用户请求的token实例。

 		如果请求是没有经过身份认证的。如果没有请求上下文，那么`request.auth` 的值是 `None`.

#### Request.method

​	`request.method` 返回的是代表请求方法的大写的字符串。基于 PUT、PACTH、DELETE提交也是支持的。

#### Request.content_type

​	`request.content_type` 返回的是HTTP请求体中代表没接资源的对象的字符串，如果不存在则返回一个空的字符串。

​	如果你需要获取请求中的content type 时，建议使用`content_type`属性，而不是使用`request.META.get('HTTP_CONTENT_TYPE')`,因为他提供比较灵活的基于浏览器的非表单内容的支持。

### Response 

> 与基本的 HttpResponse 对象不同，TemplateResponse 对象保留了视图提供的用于计算响应的上下文的详细信息。直到需要时才会计算最终的响应输出，也就是在后面的响应过程中进行计算。 — *Django 文档*

​		REST framework 通过提供一个 `Response` 类来支持 HTTP 内容协商，该类允许你根据客户端请求返回不同的表现形式（如： JSON ，HTML 等）。

`		Response` 类的子类是 Django 的 `SimpleTemplateResponse`。`Response` 对象使用数据进行初始化，数据应由 Python 对象（native Python primitives）组成。然后 REST framework 使用标准的 HTTP 内容协商来确定它应该如何渲染最终响应的内容。

当然，您也可以不使用 `Response` 类，直接返回常规 `HttpResponse` 或 `StreamingHttpResponse` 对象。 使用 `Response` 类只是提供了一个更好的交互方式，它可以返回多种格式。

除非由于某种原因需要大幅度定制 REST framework ，否则应该始终对返回 `Response` 对象的视图使用 `APIView` 类或 `@api_view` 装饰器。这样做可以确保视图执行内容协商，并在视图返回之前为响应选择适当的渲染器。

#### Response()

 ```python
Response(data, status=None, template_name=None, headers=None, content_type=None)
 ```

不同通常的`HTTPResponse`,不用使用`Response`对象来渲染内容。可以直接将为渲染的内容传入。

由于 `Response` 类使用的渲染器不能处理复杂的数据类型（比如 Django 的模型实例），所以需要在创建 `Response` 对象之前将数据序列化为基本的数据类型。

你可以使用 REST framework 的 `Serializer` 类来执行序列化的操作，也可以用自己的方式来序列化。

```python
# 参数
data 响应的序列化的数据
status 响应的状态码，默认的是200.
template_name 如果选择使用 HTMLRenderer时，模版的名字。
headers: 字典形式的HTTP 用在响应头部内容。
content_type: 响应内容的类型，通常上，被自动的设置为事先协商的内容。但是有一些情况你需要设置特定明确的内容类型。
```

##### Attribute：

​	**data**

 			响应中没有渲染、未序列化的数据。

 	**status_code**

 			响应的数字状态码

​      **content**

​        	将会返回的响应内容，必须先调用 `.render()` 方法，才能访问 `.content` 。		

​	  **template_name**

​			只有在 response 的渲染器是 `HTMLRenderer` 或其他自定义模板渲染器时才需要提供。

​		**accepted_renderer**

​			用于将会返回的响应内容的渲染器实例。

​			从视图返回响应之前由 `APIView` 或 `@api_view` 自动设置。

​	**accepted_media_type**

​			内容协商阶段选择的媒体类型。

​			从视图返回响应之前由 `APIView` 或 `@api_view` 自动设置。

​	**renderer_context**

​			将传递给渲染器的 `.render()` 方法的附加的上下文信息字典。

​			从视图返回响应之前由 `APIView` 或 `@api_view` 自动设置。

#### Standard HttpResponse attributes

 	`Response` 是来自`SimpleTemplateResponse`的扩展。所有可用的属性和方法都是可用的。例如你可以设置请求头使用标准的方法。	

```python
response = Response()
response['Cache-Control'] = 'no-cache'
```

**.render()**

​		与其他任何 `TemplateResponse` 一样，调用此方法将响应的序列化数据呈现为最终响应内容。响应内容将设置为在 `accepted_renderer` 实例上调用 `.render(data，accepted_media_type，renderer_context)` 方法的结果。

​		通常不需要自己调用 `.render()` ，因为它是由 Django 处理的。

### Status Code

​	直接使用数字状态码进行返回是不推荐的。REST framework提供了一种方法可以使你的状态码更加明显而且可读性更高。

```python
from rest_framework import status
from rest_framework.response import Response

def empty_view(self):
  	content  = {'please move along':'nothing to see here!'}
    return Response(content, status=status.HTTP_404_NOT_FOUND)
```

状态模块中包含的全部HTTP状态代码如下所示。

该模块还包括一组帮助函数，用于测试状态代码是否在给定范围内。

```python
from rest_framework import status
from rest_framework.test import APITestCase

class ExampleTestCase(APITestCase):
    def test_url_root(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))
```

#### Informational-1XX

```
HTTP_100_CONTINUE
HTTP_101_SWITCHING_PROTOCOLS
```

#### Successful-2XX

```
HTTP_200_OK
HTTP_201_CREATED
HTTP_202_ACCEPTED
HTTP_203_NON_AUTHORITATIVE_INFORMATION
HTTP_204_NO_CONTENT
HTTP_205_RESET_CONTENT
HTTP_206_PARTIAL_CONTENT
HTTP_207_MULTI_STATUS
HTTP_208_ALREADY_REPORTED
HTTP_226_IM_USED
```

#### Redirection - 3XX

```
HTTP_300_MULTIPLE_CHOICES
HTTP_301_MOVED_PERMANENTLY
HTTP_302_FOUND
HTTP_303_SEE_OTHER
HTTP_304_NOT_MODIFIED
HTTP_305_USE_PROXY
HTTP_306_RESERVED
HTTP_307_TEMPORARY_REDIRECT
HTTP_308_PERMANENT_REDIRECT
```

#### Client Error -4XX

4xx 类的状态码似乎看起来好像是客户端发生错误，请求头中应当包含实体的错误状况，不管是永久的还是临时的。

```python
HTTP_400_BAD_REQUEST
HTTP_401_UNAUTHORIZED
HTTP_402_PAYMENT_REQUIRED
HTTP_403_FORBIDDEN
HTTP_404_NOT_FOUND
HTTP_405_METHOD_NOT_ALLOWED
HTTP_406_NOT_ACCEPTABLE
HTTP_407_PROXY_AUTHENTICATION_REQUIRED
HTTP_408_REQUEST_TIMEOUT
HTTP_409_CONFLICT
HTTP_410_GONE
HTTP_411_LENGTH_REQUIRED
HTTP_412_PRECONDITION_FAILED
HTTP_413_REQUEST_ENTITY_TOO_LARGE
HTTP_414_REQUEST_URI_TOO_LONG
HTTP_415_UNSUPPORTED_MEDIA_TYPE
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
HTTP_417_EXPECTATION_FAILED
HTTP_422_UNPROCESSABLE_ENTITY
HTTP_423_LOCKED
HTTP_424_FAILED_DEPENDENCY
HTTP_426_UPGRADE_REQUIRED
HTTP_428_PRECONDITION_REQUIRED
HTTP_429_TOO_MANY_REQUESTS
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE
HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
```

#### Server Error -5XX

响应的状态码如果返回的是5开头的数字的话，那么就意味着服务端可能发生了异常或者不能正常的解析请求，请求头中应当包含实体的错误状况，不管是永久的还是临时的。

```
HTTP_500_INTERNAL_SERVER_ERROR
HTTP_501_NOT_IMPLEMENTED
HTTP_502_BAD_GATEWAY
HTTP_503_SERVICE_UNAVAILABLE
HTTP_504_GATEWAY_TIMEOUT
HTTP_505_HTTP_VERSION_NOT_SUPPORTED
HTTP_506_VARIANT_ALSO_NEGOTIATES
HTTP_507_INSUFFICIENT_STORAGE
HTTP_508_LOOP_DETECTED
HTTP_509_BANDWIDTH_LIMIT_EXCEEDED
HTTP_510_NOT_EXTENDED
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED
```

### View

REST framework 提供了APIView.他是Django中的View的子类。

APIView在以下几个方面不同于Django中普通的View：

>- 传入到视图方法中的是REST framework的Request对象，而不是Django的HttpRequeset对象；
>- 视图方法可以返回REST framework的Response对象，视图会为响应数据设置（render）符合前端要求的格式；
>- 任何APIException异常都会被捕获到，并且处理成合适的响应信息；
>- 在进行dispatch()分发前，会对请求进行身份认证、权限检查、流量控制。

使用APIView和使用原生的View大体相同。通常，请求来了之后根据请求的类型进行分发。此外,大量的属性可以设置类,控制API的各个方面的限制策略。

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
```

​		Django REST框架的APIView、GenericAPIView、各种mixin和viewset之间的完整方法、属性和关系最初可能很复杂。除了这里的文档外，Classy Django REST框架资源还为每个Django REST框架的基于类的视图提供了一个可浏览的引用，其中提供了完整的方法和属性。

#### @api_view()

​		该功能的核心是api_view装饰器，获取视图响应的HTTP方法列表。例如，这是你如何写一个非常简单的视图，只是手动返回一些数据:

```python
from rest_framework.decorators import api_view

@api_view()
def hello_world(request):
  	return Response({'message':'Hello world.'})
```

这个试图会使用默认的渲染、解析、认证，详细的方法在设置中。

默认的话，只会接受GET请求，其他的请求的方法会被返回`405 Method Not Allowed`如果需要改变的话，可以如下这么做：

```python
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})
```

#### API policy decorators

重写默认的设置，REST framework 提供了一些可以添加装饰器的方法添加到试图上。

这是装饰器必须写在api_view的装饰器之下。例如，来创建一个限流的装饰器，来控制普通用户一天只能访问一次。使用`@throttle_classes`装饰器，传入一个控制流量的类。

```python
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle

class OncePerDayUserThrottle(UserRateThrottle):
        rate = '1/day'

@api_view(['GET'])
@throttle_classes([OncePerDayUserThrottle])
def view(request):
    return Response({"message": "Hello for today! See you tomorrow!"})
```

还有如下的装饰器可以使用

```python
@render_classes(...)
@parser_classes(...)
@authentication_classes(...)
@throttle_classes(...)
@permission_classes(...)
```

#### View Scheme decorator

要覆盖基于函数的视图的默认模式生成，可以使用@schema装饰器。这必须在@api_view装饰器之后。例如:

```python
from rest_framework.decorators import api_view, schema
from rest_framework.schemas import AutoSchema

class CustomAutoSchema(AutoSchema):
    def get_link(self, path, method, base_url):
        # override view introspection here...

@api_view(['GET'])
@schema(CustomAutoSchema())
def view(request):
    return Response({"message": "Hello for today! See you tomorrow!"})
```

该装饰器接受一个AutoSchema实例、一个AutoSchema子类实例或模式文档中描述的ManualSchema实例。您可以传递None以将视图从模式生成中排除。

```python
@api_view(['GET'])
@schema(None)
def view(request):
    return Response({"message": "Will not appear in schema!"})
```

### Settings

REST framwork的配置在Django中配置文件中是以命名空间的形式存在，为`REST_FRAMEWORK`.例如你的配置文件中可以这样写：

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}
```

 #### Accessing settings

如果你需要在你的项目中访问REST framework中的配置信息。你可以使用`api_settings`,例如：

```python
from rest_framework.settings import api_settings
print(api_settings.DEFAULT_AUTHENTICATION_CLASSES)

```

`api_setting`会检查用户在settings中的配置，如果不存在的话，则返回的是用户默认的设置，任何使用字符串导入路径来引用类的设置都会自动导入并返回引用的类，而不是字符串文本。

















​		