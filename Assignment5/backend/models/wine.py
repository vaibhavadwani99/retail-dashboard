from db import db


class WineModel(db.Model):

    __tablename__ = "wine"

    id = db.Column(db.Integer, primary_key=True)
    fixed_acidity = db.Column(db.Float)
    volatile_acidity = db.Column(db.Float)
    citric_acid = db.Column(db.Float)
    residual_sugar = db.Column(db.Float)
    chlorides = db.Column(db.Float)
    free_sulfur_dioxide = db.Column(db.Float)
    total_sulfur_dioxide = db.Column(db.Float)
    density = db.Column(db.Float)
    pH = db.Column(db.Float)
    sulphates = db.Column(db.Float)
    alcohol = db.Column(db.Float)
    quality = db.Column(db.Integer)
    label = db.Column(db.String(80))

    def __init__(
        self,
        fixed_acidity,
        volatile_acidity,
        citric_acid,
        residual_sugar,
        chlorides,
        free_sulfur_dioxide,
        total_sulfur_dioxide,
        density,
        pH,
        sulphates,
        alcohol,
        quality,
        label,
    ):

        self.fixed_acidity = fixed_acidity
        self.volatile_acidity = volatile_acidity
        self.citric_acid = citric_acid
        self.residual_sugar = residual_sugar
        self.chlorides = chlorides
        self.free_sulfur_dioxide = free_sulfur_dioxide
        self.total_sulfur_dioxide = total_sulfur_dioxide
        self.density = density
        self.pH = pH
        self.sulphates = sulphates
        self.alcohol = alcohol
        self.quality = quality
        self.label = label

    @classmethod
    def qualityCountPlot(cls):

        quality = cls.query.with_entities(WineModel.quality).all()
        return quality

    # @classmethod
    # def alcoholHistogramPlot(cls):

    #     alcohol = cls.query.with_entities(WineModel.alcohol).all()
    #     return alcohol

    @classmethod
    def tsdvsfsdScatterPlot(cls):  # total sulfur dioxide vs free sulfur dioxide plot

        scatter = cls.query.with_entities(
            WineModel.total_sulfur_dioxide, WineModel.free_sulfur_dioxide
        ).all()
        return scatter

    @classmethod
    def densityvsphScatterPlot(cls):  # density vs ph scatter plot

        scatter = cls.query.with_entities(WineModel.density, WineModel.pH).all()
        return scatter

    @classmethod
    def labelcountplot(cls):  # density vs ph scatter plot

        label = cls.query.with_entities(WineModel.label).all()
        return label
