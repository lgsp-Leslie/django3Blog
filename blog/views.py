# Create your views here.
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, get_object_or_404

from blog.models import Blog, BlogType, ReadNum
from django3Blog.settings import EACH_PAGE_BLOGS_NUMBER


def get_blog_list_common_data(request, blogs_all_list):
    # blog_types = BlogType.objects.all()
    blog_dates = Blog.objects.dates('created_time', 'month', order='DESC')

    paginator = Paginator(blogs_all_list, EACH_PAGE_BLOGS_NUMBER)
    page_num = request.GET.get('page', 1)  # 获取页面参数（get请求）
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number  # 获取当前页码
    # 获取当前页码的前后各2页的页码范围
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + list(
        range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    # 获取博客分类的对应博客数量
    '''
    # 方法一：
    blog_types_list = []
    for blog_type in blog_types:
        blog_type.blog_count = Blog.objects.filter(blog_type=blog_type).count()
        blog_types_list.append(blog_type)
    '''
    # 方法二
    blog_type_count = BlogType.objects.annotate(blog_count=Count('blog'))

    # 获取日期归档对应的博客数量
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year, created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count

    context = {
        'blogs': page_of_blogs.object_list,
        'page_of_blogs': page_of_blogs,
        'page_range': page_range,
        # 'blog_types': blog_types_list,
        'blog_types': blog_type_count,
        'blog_dates': blog_dates_dict,
    }

    return context


def blog_list(request):
    blogs_all_list = Blog.objects.all()

    context = get_blog_list_common_data(request, blogs_all_list)

    return render(request, 'blog_list.html', context)


def blogs_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)

    context = get_blog_list_common_data(request, blogs_all_list)
    context['blog_type'] = blog_type

    return render(request, 'blogs_with_type.html', context)


def blogs_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(created_time__year=year, created_time__month=month)
    blog_with_date = '%s年%s月' % (year, month)

    context = get_blog_list_common_data(request, blogs_all_list)
    context['blog_with_date'] = blog_with_date

    return render(request, 'blogs_with_date.html', context)


def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    if not request.COOKIES.get('blog_%s_read_num' % blog_pk):
        if ReadNum.objects.filter(blog=blog):
            # 存在对应记录
            read_num = ReadNum.objects.get(blog=blog)
        else:
            # 不存在对应记录
            read_num = ReadNum(blog=blog)
        # 计数+1
        read_num.read_num += 1
        read_num.save()

    # 上下篇博客
    previous_blog = Blog.objects.filter(created_time__gt=blog.created_time).last()
    next_blog = Blog.objects.filter(created_time__lt=blog.created_time).first()

    blog_dates = Blog.objects.dates('created_time', 'month', order='DESC')

    context = {
        'blog': blog,
        'previous_blog': previous_blog,
        'next_blog': next_blog,
        'blog_dates': blog_dates,
    }
    # return render(request, 'blog_detail.html', context=context)
    response = render(request, 'blog_detail.html', context=context)  # 响应
    response.set_cookie('blog_%s_read_num' % blog_pk, 'true')
    return response
