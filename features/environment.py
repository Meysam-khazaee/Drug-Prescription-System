# before all
def before_all(context):
    print('Before all executed')


# before every feature
def before_feature(context, feature):
    print('Before feature executed')


# before every scenario
def before_scenario(scenario, context):
    print('Before scenario executed')


# before every step
def before_step(context, step):
    print('Before step executed')


# before every tag
def before_tag(context, tag):
    print('Before tag executed')


# after every feature
def after_feature(scenario, context):
    print('After feature executed')


# after every scenario
def after_scenario(scenario, context):
    print('After scenario executed')


# after every step
def after_step(context, step):
    print('After step executed')


# after every tag
def after_tag(context, tag):
    print('After tag executed')


# after all
def after_all(context):
    print('After all executed')