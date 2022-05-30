    NSMutableArray *array=[NSMutableArrayarrayWithCapacity:0];
    NSInteger subLength=1;
    for(int i=0;i<_strSelect.length;i++){       
     NSRange range=NSMakeRange(i, subLength);
        NSString *s=[_strSelect substringWithRange:range];
        [array addObject:s];
    }
     CGFloat w =1;//保存前一个button的宽以及前一个button距离屏幕边缘的距离
    CGFloat h =2;//用来控制button距离父视图的高
    for (int i =0; i < array.count; i++) {
        UIButton *button = [UIButtonbuttonWithType:UIButtonTypeSystem];
        button.tag =100 + i;
 
        [button setBackgroundImage:[UIImageimageNamed:@"btn.png"]forState:UIControlStateNormal];
        [button addTarget:selfaction:@selector(handleClick:)forControlEvents:UIControlEventTouchUpInside];
        [button setTitleColor:[UIColorblackColor]forState:UIControlStateNormal];
       //为button赋值
        [button setTitle:array[i] forState:UIControlStateNormal];
 
         //根据计算文字的大小来自适应按钮的大小，就是使用如下注释的代码：
//        NSDictionary *attributes = @{NSFontAttributeName:[UIFont systemFontOfSize:19]};
//        CGFloat length = [array[i] boundingRectWithSize:CGSizeMake(self.viewWorld.frame.size.width, 2000) options:NSStringDrawingUsesLineFragmentOrigin attributes:attributes context:nil].size.width;
       
    //设置button的frame
//    button.frame = CGRectMake(w, h, length + 55 , 80);
    //当button的位置超出视图边缘时换行
//    if(w + length + 15 > 320){
//        w = 1; //换行时将w置为1
//        h = h + button.frame.size.height;//距离父视图也变化
//        button.frame = CGRectMake(w, h, length + 55, 80);//重设button的frame
//    }
 
       //设置button的frame
        button.frame =CGRectMake(w, h,80 ,80);
        //当button的位置超出视图边缘时换行
        if(w +80 >self.viewWorld.frame.size.width){
            w = 1;//换行时将w置为1
            h = h + button.frame.size.height;//距离父视图也变化
            button.frame =CGRectMake(w, h,80,80);//重设button的frame
        }
        w = button.frame.size.width + button.frame.origin.x;
        [self.viewWorldaddSubview:button];
    }