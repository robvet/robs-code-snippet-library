How to give AI QR code making abilities!  

SK

    [KernelFunction("create_qr_code")]
    [Description("Create a QR code from the bing query text.")]
    [return: Description("The path to the QR code image.")]
    public async Task<string> create_qr_code(string query, int card_id)
    {
        // http encode query
        query = WebUtility.UrlEncode(query);
        var s = $"https://www.bing.com/search?q={query}++site:learn.microsoft.com&shm=cr&form=DEEPSH";
        QRCodeGenerator qrGenerator = new QRCodeGenerator();
        QRCodeData qrCodeData = qrGenerator.CreateQrCode(s, QRCodeGenerator.ECCLevel.Q);
       
        QRCode qrCode = new QRCode(qrCodeData);
        Bitmap qrCodeImage = qrCode.GetGraphic(20);
        var qrCodePath = Path.Combine(Directory.GetCurrentDirectory(), $"{card_id}.png");
        qrCodeImage.Save(qrCodePath);
        return qrCodePath;
    }