OV.ThreeModelLoader = class
{
    constructor ()
    {
        this.importer = new OV.Importer ();
        this.callbacks = null;
		this.inProgress = false;
    }

    Init (callbacks)
    {
        this.callbacks = callbacks;
    }

	SetDefaultColor (defaultColor)
	{
		this.importer.SetDefaultColor (defaultColor);
	}

	LoadFromUrlList (urls)
	{
		if (this.inProgress) {
			return;
		}

		let obj = this;
		this.inProgress = true;
        this.callbacks.onLoadStart ();
		this.importer.LoadFilesFromUrls (urls, function () {
			obj.OnFilesLoaded ();
		});
	}
	
	LoadFromFileList (files)
	{
		if (this.inProgress) {
			return;
		}

		let obj = this;
		this.inProgress = true;
        this.callbacks.onLoadStart ();
		this.importer.LoadFilesFromFileObjects (files, function () {
			obj.OnFilesLoaded ();
		});
	}

	ReloadFiles ()
	{
		if (this.inProgress) {
			return;
		}

		this.inProgress = true;
        this.callbacks.onLoadStart ();
		this.OnFilesLoaded ();		
	}
    
	OnFilesLoaded ()
	{
		let obj = this;
		this.callbacks.onImportStart ();
		OV.RunTaskAsync (function () {
			obj.importer.Import ({
				success : function (importResult) {
					obj.OnModelImported (importResult);
				},
				error : function (importError) {
					obj.callbacks.onLoadError (importError);
					obj.inProgress = false;
				}
			});
		});
	}

	OnModelImported (importResult)
	{
		let obj = this;
		this.callbacks.onVisualizationStart ();
		OV.ConvertModelToThreeMeshes (importResult.model, {
			onTextureLoaded : function () {
				obj.callbacks.onTextureLoaded ();
			},
			onModelLoaded : function (meshes) {
				obj.callbacks.onModelFinished (importResult, meshes);
				obj.inProgress = false;
			}
		});
	}

	GetImporter ()
	{
		return this.importer;
	}
};
